from django.db.models.expressions import F
from django.http import request
from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required # importando o decoration de login
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime, timedelta
from django.http.response import Http404, JsonResponse

# Create your views here.

# Lista um evento passado pela URL
def get_Evento(request, titulo_evento):
    evento = Evento.objects.get(titulo=titulo_evento)
    return HttpResponse(evento.descricao) 

# def getEventos(request):
#     eventos = Evento.objects.all()
#     return HttpResponse(eventos)

# Rederizando o HTML
@login_required(login_url='/login/') # decoration só abrirá a pagina se estiver logado, caso contrário irá direcionado para /login/, não esquecer a "/" no inicio para não concatenar
def lista_eventos(request):
    # eventos = Evento.objects.all()
    usuario = request.user # pegando o usuário logado 
    data_atual = datetime.now() - timedelta(hours=1)
    eventos = Evento.objects.filter(usuario=usuario, data_evento__gt=data_atual) # __lt= traz anterior a data_atual, __gt= traz a data_atual e os posteriores a data_atual
    dados = {'eventos': eventos, 'usuario':usuario}
    return render(request, 'agenda.html', dados)

# redirecionamento
# def index(request):
#     return redirect('/agenda')

# Redirecionamento para a pagina de login
def login_user(request):
    return render(request, 'login.html')


def login_submit(request):
    if request.POST:
        username = request.POST.get('username') # Recuperando os parametros enviados pelo formulário
        password = request.POST.get('password') # Recuperando os parametros enviados pelo formulário

        usuario = authenticate(username=username, password=password) # Fazendo a autenticação
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha invalido!")
    return redirect('/')

def logout_user(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def evento(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)
    return render(request, 'evento.html', dados)

@login_required(login_url='/login/')
def salvar(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        data_evento = request.POST.get('data_evento')
        usuario = request.user
        id_evento = request.POST.get('id_evento')
        if id_evento:
            # Evento.objects.filter(id=id_evento).update(
            #     titulo=titulo,
            #     descricao=descricao,
            #     data_evento=data_evento,
            # )
            # outra forma
            evento = Evento.objects.get(id=id_evento)
            if evento.usuario == usuario:
                evento.titulo = titulo
                evento.descricao = descricao
                evento.data_evento = data_evento
                evento.save()
        else:
            Evento.objects.create(
                titulo=titulo,
                descricao=descricao,
                data_evento=data_evento,
                usuario=usuario
            )
    return redirect('/')

@login_required(login_url='/login/')
def delete(request, id):
    try:
        evento = Evento.objects.get(id=id)
    except Exception:
        raise Http404()

    usuario = request.user
    evento = Evento.objects.get(id=id)
    if usuario == evento.usuario:
        evento.delete()
    else:
        raise Http404()
    return redirect('/')

@login_required(login_url='/login/')
def json_lista_evento(request):
    usuario = request.user
    eventos = Evento.objects.filter(usuario=usuario).values('id', 'titulo') # __lt= traz anterior a data_atual, __gt= traz a data_atual e os posteriores a data_atual
    return JsonResponse(list(eventos), safe=False)
    # return JsonResponse({'title': 'teste'}) não precisa utilizar o safe=False