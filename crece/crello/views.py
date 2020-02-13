from django.shortcuts import render
from django.forms import ModelForm
from crello.models import Tablero

def nave(request):
    return render(request,'crello/nav.html',{})

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
        # return redirect('libreria: consultar_Cliente')
    return render(request,templ,{'form':form})

