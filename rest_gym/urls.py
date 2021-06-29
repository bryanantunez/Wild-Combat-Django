from django.urls import path
from rest_gym.views import lista_eventos,detalle_evento

urlpatterns = [
    path('lista-eventos',lista_eventos,name='lista_eventos'),
    path('detalle-evento/<id>',detalle_evento,name='detalle_evento'),
]

