
# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from . import models
from .forms import UUIDUserForm, Contato
from django.http import HttpResponseRedirect


class UserCreateView(CreateView):
    model = models.UUIDUser
    template_name = 'user/form.html'
    success_url = reverse_lazy('museu:login')
    form_class = UUIDUserForm
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.set_password(obj.password)
        obj.save()
        return super(UserCreateView, self).form_valid(form)

class Home(TemplateView):
    template_name = 'core/home.html'

class Contato(CreateView):
    model = models.Contato
    template_name = 'core/contato.html'
    success_url = reverse_lazy('museu:contato')
    form_class = Contato

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(Contato, self).form_valid(form)

class Sobre(TemplateView):
    template_name = 'core/sobre.html'


