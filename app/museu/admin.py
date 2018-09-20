# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth import admin as auth

from .models import Contato


admin.site.register(Contato)
