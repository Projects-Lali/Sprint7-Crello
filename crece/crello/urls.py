from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crearT/', views.crear_tab, name='crear_tab'),
]
