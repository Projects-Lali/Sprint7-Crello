from django.shortcuts import render,redirect
from django.forms import ModelForm
from crello.models import Tablero

def index(request):
    return render(request,'crello/index.html',{})

class TableroForm(ModelForm):
    class Meta:
        model = Tablero
        fields =['nombre']

''' class ListaForm(ModelForm):
    class Meta:
        model = Lista
        fields =['nombre','fk_Tablero']

class TarjetaForm(ModelForm):
    class Meta:
        model = Tarjeta
        fields =['nombre','descripcion','fk_Lista'] '''

def crear_tab(request):
    templ = 'crello/crear_tablero.html'
    form =  TableroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('crello: index.html')# tiene que dirigir a otro
    return render(request,templ,{'form':form})

