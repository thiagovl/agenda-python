from django.db import models
from django.db.models.fields import DateTimeField
from django.contrib.auth.models import User # importando o models User do django

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='DATA DO EVENTO')
    data_criacao = models.DateTimeField(verbose_name='DATA DE CRIAÇÃO', auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) # chave estrangeira

    # Especificando o nome da tabela
    class Meta:
        db_table = 'evento'

    # Altera como será mostrado no Painel
    # def __str__(self):
    #     return self.titulo

    # Formatando a data
    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M')