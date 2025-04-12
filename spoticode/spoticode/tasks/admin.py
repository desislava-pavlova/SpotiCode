import random, string
from datetime import datetime
# Django
from django.contrib import admin
# Project
from spoticode.tasks.models import Task, TaskComment
from spoticode.web.default_values import get_deleted_user
# Other
from django_admin_listfilter_dropdown.filters import DropdownFilter


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'task_name', 'formatted_date_created', 'task_type','priority', 'related_app', 'responsible', 'status')
    search_fields = ('task_name', 'description')
    list_filter = (
        ('related_app', DropdownFilter),
        ('responsible__username', DropdownFilter),
        ('status', DropdownFilter),
        ('priority', DropdownFilter),
        ('task_type', DropdownFilter),
    )
    
    def formatted_date_created(self, obj):
        return obj.date_created.date()
    formatted_date_created.short_description = 'Date Created'
    
    def responsible(self, obj):
        return obj.responsible.username if obj.responsible else '--none--'
    
    def get_exclude(self, request, obj=None):
        if obj is None:
            return ['id', 'last_modified']
        return []
    
    def save_model(self, request, obj, form, change):
        if not obj.date_created:
                obj.date_created = datetime.now()
        else:
            try:
                old = Task.objects.get(id=obj.id)
                if old.status not in ['Cancelled', 'Completed'] and obj.status in ['Cancelled', 'Completed']:
                    obj.date_closed = datetime.now()
                
                if obj.status not in ['Cancelled', 'Completed']:
                    obj.date_closed = None
            except Task.DoesNotExist:
                pass
        super().save_model(request, obj, form, change)
        

@admin.register(TaskComment)
class TaskCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'formatted_date_created', 'user', 'task', 'comment_text')
    search_fields = ('comment_text',)
    list_filter = (
        ('user__username', DropdownFilter),
        ('task_id__task_name', DropdownFilter),
    )
    
    def user(self, obj):
        return obj.user.username if obj.user else None
    
    def task(self, obj):
        return obj.task_id.task_name if obj.task_id else None
    
    def formatted_date_created(self, obj):
        return obj.date_created.date()
    formatted_date_created.short_description = 'Date Created'
    
    def get_exclude(self, request, obj=None):
        if obj is None:
            return ['id', 'user', 'date_created']
        return []

    def save_model(self, request, obj, form, change):
        try:
            obj.user = request.user
        except AttributeError:
            obj.user = get_deleted_user()
            
        super().save_model(request, obj, form, change)
