from django.shortcuts import render, redirect
from formulario.models import Evento
from .forms import EventoForm

def home(request):
    context = {"nombre":"Clases", "tipo":"Disponibles"}
    return render(request, 'formulario/index.html', context)

def formu(request):
    return render(request,'formulario/formu.html')

def boxeo(request):
    return render(request,'formulario/boxeo.html')



def eventos(request):
    listaEventos = Evento.objects.all()
    datos = {
        'eventos':listaEventos
    }
    return render(request,'formulario/eventos.html',datos)



def lista_evento(request):
    datos = {
        'form':EventoForm()
    }
    if(request.method == 'POST'):
        formulario = EventoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Guardados correctamente'
    return render(request,'formulario/lista_evento.html',datos)

def mod_evento(request, id):
    eventos = Evento.objects.get(idEvento=id)
    datos = {

        'form':EventoForm(instance=eventos)
    }
    if(request.method == 'POST'):
        formulario = EventoForm(data=request.POST, instance=eventos)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Modificados correctamente'
    return render(request,'formulario/mod_evento.html',datos)

def borrar_evento(request, id):
    eventos = Evento.objects.get(idEvento=id)
    eventos.delete()
    return redirect(to=home)

def jiu(request):
    return render(request,'formulario/jiu.html')

def kickboxing(request):
    return render(request,'formulario/kickboxing.html')

def mma(request):
    return render(request,'formulario/mma.html')
