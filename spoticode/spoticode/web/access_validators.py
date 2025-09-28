from functools import wraps
# Django
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
# Project
from spoticode.web.routers import get_current_db


def custom_login_required(func):
    decorated_view_func = login_required(func)
    
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return decorated_view_func(request, *args, **kwargs)
        else:
            return redirect('user_login')

    return wrapper


def database_required(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        current_db = get_current_db()
        if not current_db or current_db == 'default':
            return redirect('database_choose')
        else:
            return func(request, *args, **kwargs)

    return wrapper


def can_create_or_update(func):
    actual_decorator = user_passes_test(
        lambda u: u.groups.filter(name__in=['Admin', 'Moderator', 'Editor']).exists(),
        login_url ='/unauthorized/'
    )
    
    if func:
        return actual_decorator(func)
    
    return actual_decorator


def can_delete(func):
    actual_decorator = user_passes_test(
        lambda u: u.groups.filter(name__in=['Admin', 'Moderator']).exists(),
        login_url ='/unauthorized/'
    )
    
    if func:
        return actual_decorator(func)
    
    return actual_decorator


def can_read(func):
    actual_decorator = user_passes_test(
        lambda u: u.groups.filter(name__in=['Admin', 'Moderator', 'Editor', 'Viewer']).exists(),
        login_url ='/unauthorized/'
    )
    
    if func:
        return actual_decorator(func)
    
    return actual_decorator


def is_staff(func):
    actual_decorator = user_passes_test(
        lambda u: u.is_staff,
        login_url ='/unauthorized/'
    )
    
    if func:
        return actual_decorator(func)
    
    return actual_decorator


def is_user_self(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user_id = kwargs.get('id')
        if not user_id:
            return redirect('unauthorized_access')

        target_user = get_object_or_404(User, id=user_id)

        if request.user != target_user:
            return redirect('unauthorized_access')

        return view_func(request, *args, **kwargs)
    return _wrapped_view
