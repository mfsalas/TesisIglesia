from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from apps.celula.models import Celula
from apps.celula.forms import CelulaForm
#from apps.persona.models import Persona # en apps\ministerio\views tambien esta

from .models import Celula

def index_celula(request):
	return HttpResponse("soy la pagina principal de la app adopcion")

def celula_view(request):
    if request.method == 'POST':
        form = CelulaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('celula:celula_listar')
    else:
        form = CelulaForm
    return render(request, 'celula/celula_form.html', {'form':form})

def celula_list(request):
	celula = Celula.objects.all().order_by('id')
	contexto = {'celula':evento}
	return render(request, 'celula/celula_listar.html', contexto)

def celula_edit(request, id_celula):
    celula = Evento.objects.get(id=id_celula)
    if request.method == 'GET':
        form = CelulaForm(instance=celula)
    else:
        form = CelulaForm(request.POST, instance=celula)
        if form.is_valid():
            form.save()
            return redirect('celula:celula_listar')
    return render(request,'celula/celula_form.html',{'form':form})

def celula_delete(request, id_celula):
    celula = Evento.objects.get(id=id_celula)
    if request.method == 'POST':
        celula.delete()
        return redirect('celula:celula_listar')
    return render(request,'celula/celula_delete.html',{'celula':celula})




class CelulaList(ListView):
	model = Celula
	template_name = 'celula/celula_listar.html'
	paginate_by = 3

class CelulaCreate(CreateView):
	model = Celula
	template_name = 'celula/celula_form.html'
	form_class = CelulaForm
	success_url = reverse_lazy('celula:celula_listar')

class CelulaUpdate(UpdateView):
	model = Celula
	#second_model = Persona	#no se xq persona
	template_name = 'celula/celula_form.html'
	form_class = CelulaForm
	success_url = reverse_lazy('celula:celula_listar')


class CelulaDelete(DeleteView):
	model = Celula
	template_name = 'celula/celula_delete.html'
	success_url = reverse_lazy('celula:celula_listar')



class BuscarView(TemplateView):
    def post(self, request, *args, **kwargs):
        buscar = request.POST['buscalo']
        celulas = Celula.objects.filter(dia_celula__contains=buscar)
        return render(request,'celula/buscar.html',
        {'celulas':celulas, 'celu' : True})
