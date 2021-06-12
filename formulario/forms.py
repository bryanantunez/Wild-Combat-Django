from django import forms
from django.forms import ModelForm
from .models import Evento

class EventoForm(ModelForm):
    class Meta:
        model = Evento
        fields = ['idEvento', 'nombreEvento', 'fechaEvento', 'deporte']

