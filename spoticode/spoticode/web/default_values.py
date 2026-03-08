import threading
# Django
from django.apps import apps
from django.contrib.auth.models import User


def get_app_choices():    
    app_choices = [("all", "All Apps")]
    
    for app_config in apps.get_app_configs():
            if app_config.name.__contains__('dropdown'):
                continue 
            app_choices.append((app_config.label, app_config.verbose_name))
            
    return app_choices


def get_deleted_user():
    try:
        return User.objects.get(username='deleted.user')
    except User.DoesNotExist:
        return User.objects.create(
            username='deleted.user',
            email='deleted.user@spoticode.com',
            is_superuser=False,
            is_staff=False,
            is_active=False
            )


def get_unknown_user():
    try:
        return User.objects.get(username='unknown.user')
    except User.DoesNotExist:
        return User.objects.create(
            username='unknown.user',
            email='unknown.user@spoticode.com',
            is_superuser=False,
            is_staff=False,
            is_active=False
            )
