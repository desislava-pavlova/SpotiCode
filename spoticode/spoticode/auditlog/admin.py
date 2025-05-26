# Django
from django.contrib import admin
# Project
from spoticode.auditlog.models import AuditLog
# Other
from django_admin_listfilter_dropdown.filters import DropdownFilter


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'object_id', 'table_name', 'column_name', 'action', 'old_value', 'new_value', 'last_modified', 'user')
    search_fields = ('table_name', 'column_name', 'old_value', 'new_value')
    list_filter = (
        ('table_name', DropdownFilter),
        ('column_name', DropdownFilter),
        ('action', DropdownFilter),
        ('user__username', DropdownFilter),
    )
    
    def get_exclude(self, request, obj=None):
        if obj is None:
            return ['id',]
        return []
