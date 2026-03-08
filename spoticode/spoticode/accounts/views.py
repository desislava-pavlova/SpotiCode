from datetime import datetime
# Django
from django.urls import reverse
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, login, authenticate, update_session_auth_hash
from django.contrib.auth.models import User, Group
# Project
from spoticode.accounts.forms import RegisterUserForm, EditUserForm, PasswordChangeForm
from spoticode.web.access_validators import custom_login_required, is_staff, is_user_self, database_required
from spoticode.web.routers import set_current_db



# ---------- Account Views ---------- #
# -- Log in
def log_in(request):
    error_message = ""
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.last_login is None:
                login(request, user)
                return redirect('user_first_login', id=user.id)
            else:
                login(request, user)
                return redirect('database_choose')
        else:
            error_message = 'Your username or password is incorrect.'
    
    context = {
        'curr_year': datetime.now().year,
        'error_message': error_message,
    }
    
    return render(request, 'accounts/login.html', context)


# -- Log Out
@custom_login_required
def log_out(request):
    logout(request)
    return redirect(reverse('homepage'))


# -- Choose Database
@custom_login_required
def choose_database(request): 
    available_dbs = []
    
    for db in settings.ACTIVE_DATABASES:
        try:
            if User.objects.using(db).filter(username=request.user.username).exists():
                available_dbs.append(db)
        except Exception:
            continue
    available_dbs = sorted(available_dbs)
    
    if request.method == "POST":
        db_choice = request.POST.get("database")
        if db_choice in available_dbs:
            request.session["db_choice"] = db_choice
            set_current_db(db_choice)
            
            return redirect("homepage")
        
    context = {
        'curr_year': datetime.now().year,
        'available_dbs': available_dbs,
    }

    return render(request, "accounts/choose-database.html", context)


# -- Register User
@custom_login_required
@database_required
@is_staff
def register_user(request):
    form = RegisterUserForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('homepage')
    
    context = {
        'curr_year': datetime.now().year,
        'form': form,
    }

    return render(request, 'accounts/register.html', context)


# -- First-time Log In
@custom_login_required
@is_user_self
def first_login_user(request, id):
    user = get_object_or_404(User, id=id)
    form = PasswordChangeForm(user, request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            viewer_group, created = Group.objects.get_or_create(name='Viewer')
            user.groups.add(viewer_group)
            return redirect('database_choose')
    
    context = {
        'curr_year': datetime.now().year,
        'form': form,
    }

    return render(request, 'accounts/first-login-user.html', context)


# -- Show Details
@custom_login_required
@database_required
@is_user_self
def show_details_user(request, id):
    user = get_object_or_404(User, id=id)
    user_group = user.groups.first()
    
    context = {
        'curr_year': datetime.now().year,
        'user': user,
        'user_group': user_group,
    }
    
    return render(request, 'accounts/details-user.html', context)


# -- Edit Info
@custom_login_required
@database_required
@is_user_self
def edit_user_info(request, id):
    user = get_object_or_404(User, id=id)
    form = EditUserForm(request.POST or None, instance=user)
    
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('user_details', id=user.id)
    
    context = {
        'curr_year': datetime.now().year,
        'user': user,
        'form': form,
    }
    
    return render(request, 'accounts/edit-user.html', context)


# -- Edit Password
@custom_login_required
@database_required
@is_user_self
def edit_user_password(request, id):
    user = get_object_or_404(User, id=id)
    form = PasswordChangeForm(user, request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('user_details', id=user.id)
    
    context = {
        'curr_year': datetime.now().year,
        'form': form,
    }

    return render(request, 'accounts/password-change-user.html', context)
