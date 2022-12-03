from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['email'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

    username = forms.CharField(label='', widget=forms.TextInput(attrs={"class": "form-control"})),
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={"class": "form-control"})),
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={"class": "form-control"})),
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={"class": "form-control"})),

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={"class": "form-control"})),
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class": "form-control"})),
