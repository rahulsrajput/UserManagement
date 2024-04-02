from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    fields = ['email','username','password']

    class Meta:
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control'})
        }

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email']

        widgets = {
            'email' : forms.EmailInput(attrs={'required':'required'}),
        }

class UpdateForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['email','username']