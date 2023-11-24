from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control bg-white border-left-0 border-md',
        'id': 'login-username',
        'placeholder': 'Enter your Username',
        'required': '',
        'name': 'username',
        'type': 'username'
    }),
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control bg-white border-left-0 border-md',
        'id': 'login-password',
        'placeholder': 'Enter your Password',
        'required': '',
        'name': 'password',
        'type': 'password',
    }),
    )


class SignUpForm(UserCreationForm):
    model = User
    fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'required': '',
        'name': 'username',
        'id': 'username',
        'type': 'text',
        'class': 'form-control bg-white border-left-0 border-md',
        'placeholder': 'Username',
        'maxlength': '100',
        'minlength': '4'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'required': '',
        'name': 'email',
        'id': 'email',
        'type': 'email',
        'class': 'form-control bg-white border-left-0 border-md',
        'placeholder': 'Email',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'required': '',
        'name': 'password1',
        'id': 'password1',
        'type': 'password',
        'class': 'form-control bg-white border-left-0 border-md',
        'placeholder': 'Password',
        'maxlength': '100',
        'minlength': '4'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'required': '',
        'name': 'password2',
        'id': 'password2',
        'type': 'password',
        'class': 'form-control bg-white border-left-0 border-md',
        'placeholder': 'Confirm Password',
        'maxlength': '100',
        'minlength': '4'
    }))

