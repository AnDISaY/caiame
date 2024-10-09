from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={"id": "id_email", "placeholder": "Адрес электронной почты*", }))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={"id": "id_username", "placeholder": "Имя пользователя*", }))
    password1 = forms.CharField(required=True, widget=forms.TextInput(attrs={"id": "id_password1", "placeholder": "Пароль*", }))
    password2 = forms.CharField(required=True, widget=forms.TextInput(attrs={"id": "id_password2", "placeholder": "Повторите пароль*", }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={"id": "id_username", "placeholder": "Имя пользователя*", }))
    password = forms.CharField(required=True, widget=forms.TextInput(attrs={"id": "id_password", "placeholder": "Пароль*", }))

    class Meta:
        model = User
        fields = ['username', 'password']


# class ResetForm(AuthenticationForm):
#     username = forms.CharField(required=True, widget=forms.TextInput(attrs={"id": "id_username", "placeholder": "Имя пользователя*", }))
#     new_password = forms.CharField(required=True, widget=forms.TextInput(attrs={"id": "id_password", "placeholder": "Новый пароль*", }))

#     class Meta:
#         model = User
#         fields = ['username', 'password']
