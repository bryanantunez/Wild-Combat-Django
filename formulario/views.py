from django.shortcuts import render

def home(request):
    context = {"nombre":"Clases", "tipo":"Disponibles"}
    return render(request, 'formulario/index.html', context)

def formu(request):
    return render(request,'formulario/formu.html')

def boxeo(request):
    return render(request,'formulario/boxeo.html')

def eventos(request):
    return render(request,'formulario/eventos.html')

def jiu(request):
    return render(request,'formulario/jiu.html')

def kickboxing(request):
    return render(request,'formulario/kickboxing.html')

def mma(request):
    return render(request,'formulario/mma.html')
