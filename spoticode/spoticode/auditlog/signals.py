from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from django.apps import apps
from django.db import IntegrityError, connection
from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist
# Project
from spoticode.auditlog.models import AuditLog
from spoticode.auditlog.middleware import get_current_user


# def table_exists(table_name):
    #return table_name in connection.introspection.table_names()


@receiver(pre_save)
def log_create_or_update(sender, instance, **kwargs):
    if sender.__name__ == 'AuditLog' or instance._meta.app_label in ['django_migrations', 'admin', 'auth']:
        return

    user = get_current_user()
    table_name = sender._meta.db_table
    column_name = ""

    try:
        old_instance = sender.objects.get(pk=instance.pk)
        is_update = True
        # old_value = str(old_instance)
    except ObjectDoesNotExist:
        is_update = False
        old_instance  = None

    # Now you know for sure
    print("User:", user)
    print("Table:", table_name)
    print("Object ID:", instance.pk)
    print("Action:", "UPDATE" if is_update else "CREATE")
    # print("Old value:", old_value)

    try:
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
            
                # Skip auto-generated fields (like timestamp columns, or pk)
                if field_name in ['last_modified', 'date_created', 'date_closed', instance._meta.pk.name]:
                    continue
                
                old_value = getattr(old_instance, field_name, None)
                new_value = getattr(instance, field_name, None)

                # Compare old and new values and log only if they are different
                if old_value != new_value:
                    changes.append((field_name, old_value, new_value))

            for field_name, old_value, new_value in changes:
                AuditLog.objects.create(
                    object_id=instance.pk,
                    table_name=table_name,
                    column_name=field_name,
                    action='UPDATE',
                    old_value=str(old_value) if old_value is not "" else None,
                    new_value=str(new_value) if new_value is not "" else None,
                    user=user
                )
    except IntegrityError:
        print('IntegrityError occurred.')

@receiver(post_delete)
def log_delete(sender, instance, **kwargs):
    if sender.__name__ == 'AuditLog' or instance._meta.app_label in ['django_migrations', 'admin', 'auth']:
        return

    user = get_current_user()
    table_name = sender._meta.db_table
    column_name = instance._meta.pk.name

    AuditLog.objects.create(
        object_id=instance.pk,
        table_name=table_name,
        column_name=column_name,
        action='DELETE',
        old_value=str(instance),
        user=user
    )
