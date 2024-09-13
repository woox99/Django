from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('change-password/', views.password_change, name='password-change'),
    path('change-password/successful/', views.password_change_success, name='password-change-success'),
]