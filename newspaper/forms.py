from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class ReaderCreationForm(UserCreationForm):
        class Meta:
            model = User
            fields = ['email', 'password1', 'password2']