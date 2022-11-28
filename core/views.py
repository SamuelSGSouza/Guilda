from django.shortcuts import render
from django.views.generic import TemplateView

class Index(TemplateView):
    template_name = "core/index.html"

class BemVindo(TemplateView):
    template_name = 'core/bem_vindo.html'

class Services(TemplateView):
    template_name = 'core/services.html'
# Create your views here.
