from django.urls import path

from .views import home, formu, boxeo, eventos, jiu, kickboxing, mma, lista_evento, mod_evento, borrar_evento



urlpatterns =  [

    path('',home,name='home'),

    path('formu',formu,name='formu'),

    path('boxeo',boxeo,name='boxeo'),

    path('eventos',eventos,name='eventos'),

    path('jiu',jiu,name='jiu'),

    path('kickboxing',kickboxing,name='kickboxing'),

    path('mma',mma,name='mma'),

    path('agregar-evento',lista_evento,name='lista_evento'),

    path('modificar-evento/<id>',mod_evento,name='mod_evento'),

    path('borrar-evento/<id>',borrar_evento,name='borrar_evento')

]


