from rest_framework import serializers
from formulario.models import Evento 
from formulario.models import Cliente 

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['idEvento','nombreEvento','fechaEvento','deporte']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['runCliente','nombreCliente','apellidoPaterno','apellidoMaterno','deporte']