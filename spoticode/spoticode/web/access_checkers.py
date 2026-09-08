# Project
from spoticode.web.default_values import get_db_display_name


def can_create_checker(user):
    return user.groups.filter(name__in=['Admin', 'Moderator', 'Editor']).exists()


def can_edit_checker(user):
    return user.groups.filter(name__in=['Admin', 'Moderator', 'Editor']).exists()


def can_delete_checker(user):
    return user.groups.filter(name__in=['Admin', 'Moderator']).exists()


def current_db(request):
    db_choice = request.session.get('db_choice', '')

    return {
        'current_db': 'db_choice',
        'current_db_display': get_db_display_name(db_choice) if db_choice else ''
    }
