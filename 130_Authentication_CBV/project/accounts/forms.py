from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms


class RegisterForm(UserCreationForm):
    # add any custom form fields here
    # email = forms.EmailField(required=True)
    usable_password = None

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2'] 



