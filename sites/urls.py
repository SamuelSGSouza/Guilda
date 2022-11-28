from django.urls import path
from . import views

urlpatterns = [
    path('', views.SiteIndex.as_view(), name='site_index'),
    path('landing_page', views.LandingPages.as_view(), name='landing_page'),
    path('envia_email', views.envia_email, name='envia_email'),

    ##### SESSÃO DAS VIEWS DO SITE COMERCIAL #####
    path('comercial_index', views.SiteComercialIndex.as_view(), name='site_comercial_index'),
]