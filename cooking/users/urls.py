from django.urls import path
from . import views


urlpatterns = [
    path('users', views.users, name='users'),
    path('users/<int:pk>', views.users_details, name='users_details'),
    path('profile/', views.profile, name='profile'),

    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('register/', views.register_user, name='register_user'),

    path('edit-profile/', views.edit_profile, name='edit-profile'),
]