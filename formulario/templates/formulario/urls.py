from django.urls import path
from .views import home

urlpatters = [
    path('',home,name='home'),
]