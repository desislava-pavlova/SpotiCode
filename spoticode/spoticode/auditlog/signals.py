from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
# Project
from spoticode.auditlog.models import AuditLog
from spoticode.auditlog.middleware import get_current_user

RUN_SIGNAL = True


@receiver(pre_save)
def log_create_or_update(sender, instance, **kwargs):
    if sender.__name__ == 'AuditLog' or sender._meta.db_table.startswith('django_'):
        return
    
    if not RUN_SIGNAL:
        return

    try:
        user = get_current_user() or None
        table_name = sender._meta.db_table
        column_name = ""
        
        if table_name.startswith('django_') or (table_name == 'auth_user' and user is None):
            return

        try:
            old_instance = sender.objects.get(pk=instance.pk)
            is_update = True
        except ObjectDoesNotExist:
            is_update = False
            old_instance  = None
        
        if not is_update:
            column_name = instance._meta.pk.name
            
            AuditLog.objects.create(
                object_id=instance.pk,
                table_name=table_name,
                column_name=column_name,
                action='CREATE',
                new_value=str(instance),
                user=user
            )
        else:
            changes = []
            
            for field in instance._meta.fields:
                field_name = field.name

                if field_name in ['date_modified', 'date_created', 'date_closed', instance._meta.pk.name]:
                    continue
                
                old_value = getattr(old_instance, field_name, None)
                new_value = getattr(instance, field_name, None)

                if old_value != new_value:
                    changes.append((field_name, old_value, new_value))

            for field_name, old_value, new_value in changes:
                AuditLog.objects.create(
                    object_id=instance.pk,
                    table_name=table_name,
                    column_name=field_name,
                    action='UPDATE',
                    old_value=None if old_value is None else str(old_value),
                    new_value=None if new_value is None else str(new_value),
                    user=user
                )
    except IntegrityError as e:
        print(f'IntegrityError occurred in Audit Log: {e}.')
        pass


@receiver(post_delete)
def log_delete(sender, instance, **kwargs):
    if sender.__name__ == 'AuditLog':
        return
    
    if not RUN_SIGNAL:
        return

    user = get_current_user() or None
    table_name = sender._meta.db_table
    column_name = instance._meta.pk.name
        
    if table_name.startswith('django_') or (table_name == 'auth_user' and user is None):
        return

    AuditLog.objects.create(
        object_id=instance.pk,
        table_name=table_name,
        column_name=column_name,
        action='DELETE',
        old_value=str(instance),
        user=user
    )
