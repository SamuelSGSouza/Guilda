from django.urls import path 
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('Bem_Vindo', views.BemVindo.as_view(), name='bem_vindo'),
    path('Serviços', views.Services.as_view(), name='services')
]
