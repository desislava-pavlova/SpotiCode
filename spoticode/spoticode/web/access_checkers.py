def can_create_checker(user):
    return user.groups.filter(name__in=['Admin', 'Moderator', 'Editor']).exists()


def can_edit_checker(user):
    return user.groups.filter(name__in=['Admin', 'Moderator', 'Editor']).exists()


def can_delete_checker(user):
    return user.groups.filter(name__in=['Admin', 'Moderator']).exists()


def current_db(request):
    return {
        'current_db': request.session.get('db_choice', '')
    }
