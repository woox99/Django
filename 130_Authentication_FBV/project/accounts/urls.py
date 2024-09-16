from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('change-password/', views.password_change, name='password-change'),
    path('change-password/done/', views.password_change_done, name='password-change-done'),
]