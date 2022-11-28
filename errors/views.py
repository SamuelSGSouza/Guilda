from django.shortcuts import render
from django.views.generic import TemplateView

def error404(request, exception):
    return render(request, 'errors/error404.html')
