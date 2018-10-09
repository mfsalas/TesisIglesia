from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.entrada.models import Entrada
from apps.entrada.forms import EntradaForm

from apps.persona.models import Persona


def index_entrada(request):
	return HttpResponse("soy la pagina principal de la app adopcion")

def entrada_view(request):
    if request.method == 'POST':
        form = EntradaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('entrada:entrada_listar')
    else:
        form = EntradaForm
    return render(request, 'entrada/entrada_form.html', {'form':form})

def entrada_list(request):
	entrada = Entrada.objects.all().order_by('id')
	contexto = {'entrada':entrada}
	return render(request, 'entrada/entrada_list.html', contexto)

def entrada_edit(request, id_entrada):
    entrada = Entrada.objects.get(id=id_entrada)
    if request.method == 'GET':
        form = EntradaForm(instance=entrada)
    else:
        form = EntradaForm(request.POST, instance=entrada)
        if form.is_valid():
            form.save()
            return redirect('entrada:entrada_listar')
    return render(request,'entrada/entrada_form.html',{'form':form})

def entrada_delete(request, id_entrada):
    entrada = Entrada.objects.get(id=id_entrada)
    if request.method == 'POST':
        entrada.delete()
        return redirect('entrada:entrada_listar')
    return render(request,'entrada/entrada_delete.html',{'entrada':entrada})




class EntradaList(ListView):
	model = Entrada
	template_name = 'entrada/entrada_list.html'
	paginate_by = 3

class EntradaCreate(CreateView):
	model = Entrada
	template_name = 'entrada/entrada_form.html'
	form_class = EntradaForm
	success_url = reverse_lazy('entrada:entrada_listar')

class EntradaUpdate(UpdateView):
	model = Entrada
	second_model = Persona
	template_name = 'entrada/entrada_form.html'
	form_class = EntradaForm
	success_url = reverse_lazy('entrada:entrada_listar')


class EntradaDelete(DeleteView):
	model = Entrada
	template_name = 'entrada/entrada_delete.html'
	success_url = reverse_lazy('entrada:entrada_listar')
