"""agenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView # Redirecionamento

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', views.lista_eventos),
    path('agenda/evento/salvar', views.salvar),
    path('agenda/evento/', views.evento),
    path('login/', views.login_user),
    path('login/submit', views.login_submit),
    path('logout/', views.logout_user),
    path('', RedirectView.as_view(url='/agenda/')),
    # path('', views.index), # redirecionamento
    path('evento/<titulo_evento>', views.get_Evento),
    # path('eventos/', views.getEventos),
]

# Para o metodo GET deve ter a "/" no final, para POST não