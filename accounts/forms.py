from django.contrib.auth.forms import UserCreationForm, UserChangeForm, User
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
        )
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': ' '}),
            'email': forms.EmailInput(attrs={'placeholder': ' '}),
            'first_name': forms.TextInput(attrs={'placeholder': ' '}),
            'last_name': forms.TextInput(attrs={'placeholder': ' '}),
            'password1': forms.PasswordInput(attrs={'placeholder': ' '}),
            'password2': forms.PasswordInput(attrs={'placeholder': ' '})
        }


class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'avatar'
        )
