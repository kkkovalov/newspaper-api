from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class ReaderCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, max_length=30, empty_value="")
    
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)