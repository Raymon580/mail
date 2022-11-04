from django import forms

from .models import User


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'First Name', 'name': 'firstName'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Last Name', 'name': 'lastName'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'type': 'email', 'placeholder': 'Email', 'name': 'email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Password', 'name': 'password'}),
        }