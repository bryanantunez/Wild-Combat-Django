from django.urls import path
from rest_gym.views import lista_eventos

urlpatterns = [
    path('lista_eventos',lista_eventos,name='lista_eventos');
    
]