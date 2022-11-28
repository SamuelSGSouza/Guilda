from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import EmailMultiAlternatives


class SiteIndex(TemplateView):
    template_name = 'sites/sites.html'

class LandingPages(TemplateView):
    template_name = 'sites/landing_page.html'

##### SESSÃO DAS VIEWS DO SITE COMERCIAL #####
class SiteComercialIndex(TemplateView):
    template_name = 'sites/comercial/index.html'

##### FIM SESSÃO DAS VIEWS DO SITE COMERCIAL #####



def envia_email(request):
    dados = request.GET
    subject, from_email, to = 'Contato', 'samuels.g.desouza@gmail.com', 'samuels.g.desouza@gmail.com'
    text_content = 'Mensagem de Contato'
    html_content = (f'''
    <h1>Olá, Gostaria de entrar em contato!</h1>
    <h2>Nome: {dados.get('nome')}</h2>
    <h2>Assunto: {dados.get('assunto')}</h2>
    <h2>Email: {dados.get('email')}</h2>
    <h3>{dados.get('mensagem')}</h3>
    

    Att: Cliente da Guilda | Guilda
    ''')
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    return render(request, 'sites/sites.html')
