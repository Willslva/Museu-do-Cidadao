#coding:utf-8
from __future__ import unicode_literals

from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import UUIDUser, Contato

# User: create
class UUIDUserForm(forms.ModelForm):
    class Meta:
        model = UUIDUser
        fields = ('username','first_name', 'last_name', 'password', 'email')
        labels = {
        'first_name': 'Primeiro Nome',
        'last_name': 'Sobrenome',
        'username': 'Nome de Usuário',
        'email': 'E-mail',
        'password': 'Senha',
    }
        widgets={
            'password': forms.PasswordInput()
}

class Contato(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ('nome','email','assunto','mensagem')
        labels = {
        'nome': 'Nome',
        'email': 'E-mail',
        'assunto': 'Assunto',
        'mensagem': 'Mensagem',
    }
    