# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.urls import include, path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from . import views as core

app_name = 'museu'

urlpatterns = [
	 # Login
     path('login/', auth_views.LoginView.as_view(template_name='user/auth.html'), name='login'),

    # Logout
     path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    #Cadastro de usuario
     path('usuarios/novo/', core.UserCreateView.as_view(), name='user-create'),

    #Cadastro de exposicao
     path('exposicao/novo/', core.Exposicao.as_view(), name='exposicao-create'),

    #Exibição de exposições
     path('exposicoes/', core.ListExposicao.as_view(), name='exposicao-list'),

    #Home
     path('', core.Home.as_view(), name='home'),

    #Contato
     path('contato/', core.Contato.as_view(), name='contato'),

    #Sobre
     path('sobre/', core.Sobre.as_view(), name='sobre'),


]
