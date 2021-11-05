from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento

# Create your views here.

# Lista um evento passado pela URL
def get_Evento(request, titulo_evento):
    evento = Evento.objects.get(titulo=titulo_evento)
    return HttpResponse(evento.descricao) 

# def getEventos(request):
#     eventos = Evento.objects.all()
#     return HttpResponse(eventos)

# Rederizando o HTML
def lista_eventos(request):
    eventos = Evento.objects.all()
    usuario = request.user # pegando o usuário logado 
    # eventos = Evento.objects.filter(usuario=usuario)
    dados = {'eventos': eventos, 'usuario':usuario}
    return render(request, 'agenda.html', dados)

# redirecionamento
# def index(request):
#     return redirect('/agenda')