from django.shortcuts import render
from rest_framework import status
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
        print(data)
        serializer = EventoSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def detalle_evento(request,id):
    try:
        evento = Evento.objects.get(idEvento=id)
    except Evento.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method =='GET':
        serializer = EventoSerializer(evento)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EventoSerializer(evento,data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

    elif request.method =='DELETE':
        evento.delete()
        return Response(status=status.HTTP_404_NOT_CONTENT)
