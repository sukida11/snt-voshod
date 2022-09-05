from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *


# Форма для регистрации пользователей
class RegUserForm(UserCreationForm):

	# поля в этой форме с атрибутами
	username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':'form-control'}))
	password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-control'}))
	password2 = forms.CharField(label='Повторить пароль', widget=forms.PasswordInput(attrs={'class':'form-control'}))
	email = forms.CharField(label='Email(Ваша электронная почта)', widget=forms.EmailInput(attrs={'class':'form-control'}))
	first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class':'form-control'}))

	# переопределение аттрибутов род. класса
	class Meta:
		model = User
		fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name')


# форма авторизации пользователей
class AuthUserForm(AuthenticationForm):
	username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':'form-control', 'style': 'max-width: 500px;'}))
	password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-control', 'style': 'max-width: 500px;'}))
