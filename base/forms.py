from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import ContactCard


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control bg-white border-left-0 border-md',
        'id': 'login-username',
        'placeholder': 'Username',
        'required': '',
        'name': 'username',
        'type': 'username'
    }),
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control bg-white border-left-0 border-md',
        'id': 'login-password',
        'placeholder': 'Password',
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

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already in use.')
        return email


class ContactCardForm(forms.ModelForm):
    class Meta:
        model = ContactCard
        fields = ('full_name', 'email', 'phone_number', 'address', 'location')

        widgets = {
            'full_name': forms.TextInput(attrs={
                'required': '',
                'name': 'full_name',
                'id': 'full_name',
                'type': 'text',
                'class': 'form-control bg-white border-left-0 border-md',
                'placeholder': 'Full Name / Company Name',
                'maxlength': '100',
                'minlength': '4'
            }),
            'email': forms.EmailInput(attrs={
                'required': '',
                'name': 'email',
                'id': 'email',
                'type': 'email',
                'class': 'form-control bg-white border-left-0 border-md',
                'placeholder': 'Email',
            }),
            'phone_number': forms.NumberInput(attrs={
                'required': '',
                'name': 'phone_number',
                'id': 'phone_number',
                'type': 'number',
                'class': 'form-control bg-white border-left-0 border-md',
                'placeholder': 'Enter your phone number.',
                'maxlength': '10',
                'minlength': '10'
            }),
            'address': forms.TextInput(attrs={
                'required': '',
                'name': 'address',
                'id': 'address',
                'type': 'text',
                'class': 'form-control bg-white border-left-0 border-md',
                'placeholder': 'Address',
                'maxlength': '100',
                'minlength': '4'
            }),
            'location': forms.TextInput(attrs={
                'name': 'location',
                'id': 'location',
                'type': 'text',
                'class': 'form-control bg-white border-left-0 border-md',
                'placeholder': 'Enter the map location for your physical store.',
                'maxlength': '100',
                'minlength': '4'
            })
        }


class EditContactCardForm(forms.ModelForm):
    class Meta:
        model = ContactCard
        exclude = ('user',)
        fields = ('full_name', 'email', 'phone_number', 'address', 'location')

        widgets = {
            'full_name': forms.TextInput(attrs={
                'required': '',
                'name': 'full_name',
                'id': 'full_name',
                'type': 'text',
                'class': 'form-control bg-white border-left-0 border-md',
                'placeholder': 'Full Name / Company Name',
                'maxlength': '100',
                'minlength': '4'
            }),
            'email': forms.EmailInput(attrs={
                'required': '',
                'name': 'email',
                'id': 'email',
                'type': 'email',
                'class': 'form-control bg-white border-left-0 border-md',
                'placeholder': 'Email',
            }),
            'phone_number': forms.NumberInput(attrs={
                'required': '',
                'name': 'phone_number',
                'id': 'phone_number',
                'type': 'number',
                'class': 'form-control bg-white border-left-0 border-md',
                'placeholder': 'Enter your phone number.',
                'maxlength': '10',
                'minlength': '10'
            }),
            'address': forms.TextInput(attrs={
                'required': '',
                'name': 'address',
                'id': 'address',
                'type': 'text',
                'class': 'form-control bg-white border-left-0 border-md',
                'placeholder': 'Address',
                'maxlength': '100',
                'minlength': '4'
            }),
            'location': forms.TextInput(attrs={
                'name': 'location',
                'id': 'location',
                'type': 'text',
                'class': 'form-control bg-white border-left-0 border-md',
                'placeholder': 'Enter the map location e.g. for your physical store.',
                'maxlength': '100',
                'minlength': '4'
            })
        }
