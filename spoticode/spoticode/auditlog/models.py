import uuid
# Django
from django.db import models
from django.contrib.auth.models import User
# Project
from spoticode.web.default_values import get_deleted_user, get_unknown_user


class AuditLog(models.Model):
    ACTION_CHOICES = [
        ('CREATE', 'Create'),
        ('UPDATE', 'Update'),
        ('DELETE', 'Delete'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True,
                          db_column='id', verbose_name='ID')
    object_id = models.CharField(max_length=100,
                                 db_column='object_id', verbose_name='Object ID')
    table_name = models.CharField(max_length=100, 
                                  db_column='table_name', verbose_name='Table Name')
    column_name = models.CharField(max_length=250, 
                                   db_column='column_name', verbose_name='Column Name')
    action = models.CharField(max_length=10, choices=ACTION_CHOICES, 
                              db_column='action', verbose_name='Action')
    old_value = models.CharField(null=True, blank=True, 
                                 db_column='old_value', verbose_name='Old Value')
    new_value = models.CharField(null=True, blank=True, 
                                 db_column='new_value', verbose_name='New Value')
    last_modified = models.DateTimeField(auto_now_add=True, 
                                         db_column='last_modified', verbose_name='Last Modified')
    user = models.ForeignKey(User, to_field='username', on_delete=models.SET(get_deleted_user), 
                             blank=True, default=get_unknown_user, 
                             db_column='user', verbose_name='User')

    def __str__(self):
        return f"{self.action} {self.model_name} ({self.object_pk})"
    
    class Meta:
        db_table = 'audit_log'
        ordering = ('-last_modified', )
        verbose_name = 'Audit Log'
        verbose_name_plural = 'Audit Logs'
