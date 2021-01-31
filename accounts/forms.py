from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, UsernameField
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': ' '})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': ' '})

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

        widgets = {
            'username': forms.TextInput(attrs={'style': 'margin-top: 6px;'}),
            'email': forms.EmailInput(attrs={'style': 'margin-top: 6px;'}),
            'first_name': forms.TextInput(attrs={'style': 'margin-top: 6px;'}),
            'last_name': forms.TextInput(attrs={'style': 'margin-top: 6px;'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control mt-2'}),
        }


class CustomUserLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'placeholder': ' '}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': ' '}))
