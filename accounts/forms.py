# coding=utf-8

from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Usuario


class UserAdminCreationForm(UserCreationForm):

    class Meta:
        model = Usuario
        fields = ['username', 'email']


class UserAdminForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'nome', 'is_active', 'is_staff']