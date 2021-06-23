from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from formulario.models import Evento
from .serializers import EventoSerializer
@csrf_exempt
@api_view(['GET','POST'])

def lista_eventos(request):
    if request.method == 'GET':
        evento = Evento.objects.all()
        serializer = EventoSerializer(evento, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EventoSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

