from django.urls import path, include
# Project
from spoticode.accounts import views


urlpatterns = [
    path('login/', views.log_in, name='user_login'),
    path('logout/', views.log_out, name='user_logout'),
    path('register/', views.register_user, name='user_register'),
   
    path('<int:id>/', include([
        path('first_login/', views.first_login_user, name='user_first_login'),
        path('details/', views.show_details_user, name='user_details'),
        path('edit/', views.edit_user_info, name='user_edit'),
        path('password_change/', views.edit_user_password, name='user_password_change'),
    ])),
]
