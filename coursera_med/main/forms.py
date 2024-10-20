from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserDocuments


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={"id": "id_email", "placeholder": "Адрес электронной почты*", }))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={"id": "id_username", "placeholder": "Имя пользователя*", }))
    # first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={"id": "id_first_name", "placeholder": "Имя*", }))
    # last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={"id": "id_last_name", "placeholder": "Фамилия*", }))
    password1 = forms.CharField(required=True, widget=forms.TextInput(attrs={"id": "id_password1", "placeholder": "Пароль*", }))
    password2 = forms.CharField(required=True, widget=forms.TextInput(attrs={"id": "id_password2", "placeholder": "Повторите пароль*", }))

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={"id": "id_username", "placeholder": "Имя пользователя*", }))
    password = forms.CharField(required=True, widget=forms.TextInput(attrs={"id": "id_password", "placeholder": "Пароль*", }))

    class Meta:
        model = User
        fields = ['username', 'password']



class UserDocumentsForm(forms.ModelForm):
    class Meta:
        model = UserDocuments
        fields = ['passport_front', 'passport_back', 'diploma', 'certificate', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':"documents__input"})
