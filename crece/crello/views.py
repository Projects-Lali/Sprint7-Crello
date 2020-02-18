from django.shortcuts import render,redirect,get_object_or_404
from django.forms import ModelForm
from .models import *

def index(request):
    return render(request,'crello/index.html',{})

class TableroForm(ModelForm):
    class Meta:
        model = Tablero
        fields =['nombre']

class ListaForm(ModelForm):
    class Meta:
        model = Lista
        fields =['nombre']

class TarjetaForm(ModelForm):
    class Meta:
        model = Tarjeta
        fields =['nombre','descripcion']

def crear_tab(request):
    templ = 'crello/crear_tablero.html'
    form =  TableroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('consultar_tab')
    return render(request,templ,{'form':form})

def crear_lista(request,id):
    templ = 'crello/crear_Lista.html/'
    form =  ListaForm(request.POST or None)
    info_Tablero = get_object_or_404(Tablero, pk=id)
    contexto={'form':form,'info_Tablero':info_Tablero}
    if form.is_valid():        
        lista=form.save(commit=False)
        lista.fk_Tablero=info_Tablero
        lista.save()
        return redirect('consultar_lista',id)
    return render(request,templ,contexto)

def consultar_tab(request):
    templ = 'crello/contenedorTablero.html'
    listado_tablero=Tablero.objects.all()
    contexto={}
    contexto['objectlist']=listado_tablero
    return render(request,templ,contexto)

def consultar_lista(request,id):
    templ = 'crello/tablero.html'
    listado_lista= Lista.objects.filter(fk_Tablero = id)
    info_Tablero = get_object_or_404(Tablero, pk=id)
    contexto={'listado_lista':listado_lista,'info_Tablero':info_Tablero}    
    return render(request,templ,contexto)

def editar_tab(request,id):
    template = 'crello/editar_tablero.html'
    info_Tablero = get_object_or_404(Tablero, pk=id)
    form = TableroForm(request.POST or None, instance=info_Tablero)
    if form.is_valid():
        form.save()
        return redirect('consultar_tab')
    return render(request,template,{'form':form})

def editar_lista(request,id,fk):
    template = 'crello/editar_Lista.html'
    info_Lista = get_object_or_404(Lista, pk=id)
    form = ListaForm(request.POST or None, instance=info_Lista)
    if form.is_valid():
        form.save()
        return redirect('consultar_lista' ,fk)
    return render(request,template,{'form':form})

def eliminar_tab(request,id):
    template = 'crello/eliminar_tablero.html'
    info_Tablero = get_object_or_404(Tablero, pk=id)
    if request.method == 'POST':
        info_Tablero.delete()
        return redirect('consultar_tab')
    return render(request,template,{'info_Tablero':info_Tablero})

