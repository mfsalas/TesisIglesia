from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
import datetime
from apps.ministerio.models import Ministerios
from apps.ministerio.forms import MinisteriosForm
from apps.persona.models import Persona

def index_ministerio(request):
	return HttpResponse("soy la pagina principal de la app adopcion")

def ministerio_view(request):
    if request.method == 'POST':
        form = MinisteriosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ministerio:ministerio_listar')
    else:
        form = MinisteriosForm
    return render(request, 'ministerio/ministerio_form.html', {'form':form})

def ministerio_list(request):
	ministerio = Ministerios.objects.filter(fecha_baja_ministerio__isnull=True)
	print('a')
	contexto = {'ministerios':ministerio}
	return render(request, 'ministerio/ministerio_listar.html', contexto)

def ministerio_list_baja(request):
	ministerio = Ministerios.objects.filter(fecha_baja_ministerio__isnull=False)
	contexto = {'ministerios':ministerio}
	return render(request, 'ministerio/ministerio_listar_baja.html', contexto)

def ministerio_edit(request, pk):
    ministerio = Ministerios.objects.get(id=pk)
    if request.method == 'GET':
        form = MinisteriosForm(instance=ministerio)
    else:
        form = MinisteriosForm(request.POST, instance=ministerio)
        if form.is_valid():
            form.save()
            return redirect('ministerio:ministerio_listar')
    return render(request,'ministerio/ministerio_form.html',{'form':form})

def ministerio_delete(request, pk):
    ministerio = Ministerios.objects.get(id=pk)
    if request.method == 'POST':
	    ministerio.fecha_baja_ministerio = datetime.date.today()
	    ministerio.save()
	    return redirect('ministerio:ministerio_listar')
    return render(request,'ministerio/ministerio_delete.html',{'ministerio':ministerio})

def ministerio_restore(request, pk):
    ministerio = Ministerios.objects.get(id=pk)
    if request.method == 'GET':
        ministerio.fecha_baja_ministerio = None
        ministerio.save()
        return redirect('ministerio:ministerio_listar')
    return redirect('ministerio:ministerio_listar_baja')
