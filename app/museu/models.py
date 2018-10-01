# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import uuid


from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import AbstractUser, Group, Permission
import uuid
from datetime import datetime
from django.db import models


# CreateUpdateModel
# - - - - - - - - - - - - - - - - - - -
class CreateUpdateModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    updated_at = models.DateTimeField('atualizado em', auto_now=True)

    class Meta:
        abstract = True


# UUIDUser
# - - - - - - - - - - - - - - - - - - -
class UUIDUser(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    groups = models.ManyToManyField(Group, blank=True, related_name="uuiduser_set", related_query_name="user")
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name="uuiduser_set", related_query_name="user")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'

class Contato(models.Model):
    nome  = models.CharField(max_length=255,verbose_name='Nome')
    email = models.EmailField(max_length=255,verbose_name='E-mail')
    assunto  = models.CharField(max_length=255,verbose_name='Assunto')
    mensagem  = models.TextField(max_length=255,verbose_name='Mensagem')

    def __str__(self):
        return self.mensagem
    class Meta:
    	verbose_name = 'Contato'
    	verbose_name_plural = 'Contatos'


class Exposicao(models.Model):
    usuario = models.ForeignKey(UUIDUser,on_delete=models.CASCADE,related_name="user",verbose_name='Usuário')
    titulo = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Exposicao'
        verbose_name_plural = 'Exposicoes'
        
    def __str__(self):
        return self.titulo

class Imagem(models.Model): 
    exposicao = models.ForeignKey(Exposicao,on_delete=models.CASCADE,related_name="exposicao",verbose_name='Exposicao')
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    original = models.ImageField(
        null=True,
        blank=True,
        upload_to='galeria/original',
        )
    publicacao = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        verbose_name = 'Imagem'
        verbose_name_plural = 'Imagens'

    def __str__(self):
        return self.descricao