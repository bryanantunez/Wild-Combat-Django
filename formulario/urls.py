from django.urls import path

from .views import home, formu, boxeo, eventos, jiu, kickboxing, mma



urlpatterns =  [

    path('',home,name='home'),

    path('formu',formu,name='formu'),

    path('boxeo',boxeo,name='boxeo'),

    path('eventos',eventos,name='eventos'),

    path('jiu',jiu,name='jiu'),

    path('kickboxing',kickboxing,name='kickboxing'),

    path('mma',mma,name='mma'),

]


