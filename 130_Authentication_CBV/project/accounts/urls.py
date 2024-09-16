from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('signup/', UserRegister.as_view(), name='register'),
    path('change-password/', UserPasswordChange.as_view(), name='password-change'),
    path('change-password/done/', UserPasswordChangeDone.as_view(), name='password-change-done'),
]