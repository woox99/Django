from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    # add any custom form fields here
    # email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2'] 



