from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path(
        "change-password/",
        auth_views.PasswordChangeView.as_view(
            template_name="registration/password_change.html", # direct render to custom template
            success_url=reverse_lazy('password-change-success'), # redirect to custom url pattern
        ),
        name='password-change'
    ),
    path('change-password/done/', views.password_change_success, name='password-change-success'),
]