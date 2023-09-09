from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User

class RegistrationForm(ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password']

class LoginForm(ModelForm):
    class Meta:
        model=User
        fields=['username','password']
