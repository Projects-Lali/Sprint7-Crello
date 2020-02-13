from django.urls import path
from . import views

urlpatterns = [
    path('crearT/', views.crear_tab, name='crear_tablero'),
]
