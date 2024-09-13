from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    # add any custom form fields here

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2'] 


