from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from apps.discipulado.models import Discipulado#, Discipulador
from apps.discipulado.forms import DiscipuladosForm#, DiscipuladoresForm
from apps.persona.models import Persona

###################   					DISCIPULADOS
def index_discipulado(request):
	return HttpResponse("soy la pagina principal de la app adopcion")

def discipulado_view(request):
    if request.method == 'POST':
        form = DiscipuladosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('discipulado:discipulado_listar')
    else:
        form = DiscipuladosForm
    return render(request, 'discipulado/discipulado_form.html', {'form':form})

def discipulado_list(request):
	discipulado = Discipulado.objects.all().order_by('id')
	contexto = {'discipulado':discipulado}
	return render(request, 'discipulado_listar.html', contexto)

def discipulado_edit(request, id_discipulado):
    discipulado = Discipulado.objects.get(id=id_discipulado)
    if request.method == 'GET':
        form = DiscipuladosForm(instance=discipulado)
    else:
        form = DiscipuladosForm(request.POST, instance=discipulado)
        if form.is_valid():
            form.save()
            return redirect('discipulado:discipulado_listar')
    return render(request,'discipulado/discipulado_form.html',{'form':form})

def discipulado_delete(request, id_discipulado):
    discipulado = Discipulado.objects.get(id=id_discipulado)
    if request.method == 'POST':
        discipulado.delete()
        return redirect('discipulado:discipulado_listar')
    return render(request,'discipulado/discipulado_delete.html',{'discipulado':discipulado})

class DiscipuladoList(ListView):
	model = Discipulado
	template_name = 'discipulado/discipulado_listar.html'
	paginate_by = 3

class DiscipuladoCreate(CreateView):
	model = Discipulado
	template_name = 'discipulado/discipulado_form.html'
	form_class = DiscipuladosForm
	success_url = reverse_lazy('discipulado:discipulado_listar')

class DiscipuladoUpdate(UpdateView):
	model = Discipulado
	second_model = Persona
	template_name = 'discipulado/discipulado_form.html'
	form_class = DiscipuladosForm
	success_url = reverse_lazy('discipulado:discipulado_listar')


class DiscipuladoDelete(DeleteView):
	model = Discipulado
	template_name = 'discipulado/discipulado_delete.html'
	success_url = reverse_lazy('discipulado:discipulado_listar')

class BuscarView(TemplateView):
    def post(self, request, *args, **kwargs):
        buscar = request.POST['buscalo']
        discipulado = Discipulado.objects.filter(descripcion_discipulado__contains=buscar)
        return render(request,'discipulado/buscar.html',
        {'discipulado':discipulado, 'min' : True})
