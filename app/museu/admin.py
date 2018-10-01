# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth import admin as auth

from .models import Contato, Exposicao, Imagem

admin.site.register(Exposicao)
admin.site.register(Imagem)
admin.site.register(Contato)
