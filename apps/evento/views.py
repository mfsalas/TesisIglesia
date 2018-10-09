from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.evento.models import Evento
from apps.evento.forms import EventoForm
#from apps.persona.models import Persona # en apps\ministerio\views tambien esta

def index_evento(request):
	return HttpResponse("soy la pagina principal de la app adopcion")

def evento_view(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('evento:evento_listar')
    else:
        form = EventoForm
    return render(request, 'evento/evento_form.html', {'form':form})

def evento_list(request):
	evento = Evento.objects.all().order_by('id')
	contexto = {'evento':evento}
	return render(request, 'evento/evento_listar.html', contexto)

def evento_edit(request, id_evento):
    evento = Evento.objects.get(id=id_evento)
    if request.method == 'GET':
        form = EventoForm(instance=evento)
    else:
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('evento:evento_listar')
    return render(request,'evento/evento_form.html',{'form':form})

def evento_delete(request, id_evento):
    evento = Evento.objects.get(id=id_evento)
    if request.method == 'POST':
        evento.delete()
        return redirect('evento:evento_listar')
    return render(request,'evento/evento_delete.html',{'evento':evento})




class EventoList(ListView):
	model = Evento
	template_name = 'evento/evento_listar.html'
	paginate_by = 3

class EventoCreate(CreateView):
	model = Evento
	template_name = 'evento/evento_form.html'
	form_class = EventoForm
	success_url = reverse_lazy('evento:evento_listar')

class EventoUpdate(UpdateView):
	model = Evento
	#second_model = Persona	#no se xq persona
	template_name = 'evento/evento_form.html'
	form_class = EventoForm
	success_url = reverse_lazy('evento:evento_listar')


class EventoDelete(DeleteView):
	model = Evento
	template_name = 'evento/evento_delete.html'
	success_url = reverse_lazy('evento:evento_listar')
