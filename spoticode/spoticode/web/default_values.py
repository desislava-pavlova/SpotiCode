import threading
# Django
from django.apps import apps
from django.contrib.auth.models import User


def get_app_choices():
    """
    Dynamically generate choices for app names.
    """
    app_configs = apps.get_app_configs()
    return [(app_config.label, app_config.verbose_name) for app_config in app_configs]


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
