from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.movimiento_dinero.models import Categoria, Movimiento_Dinero
from apps.movimiento_dinero.forms import Movimiento_DineroForm, CategoriaForm
from apps.persona.forms import PersonaForm

from apps.persona.models import Persona


def index_movimiento(request):
	return HttpResponse("soy la pagina principal de la app adopcion")

def movimiento_view(request):
    if request.method == 'POST':
        form = Movimiento_DineroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movimiento:movimiento_listar')
    else:
        form = Movimiento_DineroForm
    return render(request, 'movimiento_dinero/movimiento_dinero_form.html', {'form':form})

def movimiento_list(request):
	persona = Movimiento_Dinero.objects.all().order_by('id')
	contexto = {'movimiento':movimiento}
	return render(request, 'movimiento_dinero/movimiento_dinero_list.html', contexto)

def movimiento_edit(request, id_movimiento):
    movimiento = Movimiento_Dinero.objects.get(id=id_movimiento)
    if request.method == 'GET':
        form = Movimiento_DineroForm(instance=movimiento)
    else:
        form = Movimiento_DineroForm(request.POST, instance=movimiento)
        if form.is_valid():
            form.save()
            return redirect('movimiento:movimiento_listar')
    return render(request,'movimiento_dinero/movimiento_dinero_form.html',{'form':form})

def movimiento_delete(request, id_movimiento):
    persona = Movimiento_Dinero.objects.get(id=id_movimiento)
    if request.method == 'POST':
        movimiento.delete()
        return redirect('movimiento:movimiento_listar')
    return render(request,'movimiento_dinero/movimiento_dinero_delete.html',{'movimiento':movimiento})




class MovimientoList(ListView):
	model = Movimiento_Dinero
	template_name = 'movimiento_dinero/movimiento_dinero_list.html'
	paginate_by = 3

class MovimientoCreate(CreateView):
	model = Movimiento_Dinero
	template_name = 'movimiento_dinero/movimiento_dinero_form.html'
	form_class = Movimiento_DineroForm
	success_url = reverse_lazy('movimiento:movimiento_listar')

class MovimientoUpdate(UpdateView):
	model = Movimiento_Dinero
	second_model = Persona
	template_name = 'movimiento_dinero/movimiento_dinero_form.html'
	form_class = Movimiento_DineroForm
	success_url = reverse_lazy('movimiento:movimiento_listar')


class MovimientoDelete(DeleteView):
	model = Movimiento_Dinero
	template_name = 'movimiento_dinero/movimiento_dinero_delete.html'
	success_url = reverse_lazy('movimiento:movimiento_listar')

#Categorias
def categoria_view(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria:categoria_listar')
    else:
        form = CategoriaForm
    return render(request, 'categoria/categoria_form.html', {'form':form})


def categoria_list(request):
	categoria = Categoria.objects.all().order_by('id')
	contexto = {'categoria':categoria}
	return render(request, 'categoria/categoria_list.html', contexto)

def categoria_edit(request, id_categoria):
    categoria = Categoria.objects.get(id=id_categoria)
    if request.method == 'GET':
        form = CategoriaForm(instance=categoria)
    else:
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categoria:categoria_listar')
    return render(request,'categoria/categoria_form.html',{'form':form})

def categoria_delete(request, id_categoria):
    categoria = Categoria.objects.get(id=id_categoria)
    if request.method == 'POST':
        categoria.delete()
        return redirect('categoria:categoria_listar')
    return render(request,'categoria/categoria_delete.html',{'categoria':categoria})




class CategoriaList(ListView):
	model = Categoria
	template_name = 'categoria/categoria_list.html'
	paginate_by = 3

class CategoriaCreate(CreateView):
	model = Categoria
	form_class = CategoriaForm
	template_name = 'categoria/categoria_form.html'
	success_url = reverse_lazy('categoria:categoria_listar')

class CategoriaUpdate(UpdateView):
	model = Categoria
	form_class = CategoriaForm
	template_name = 'categoria/categoria_form.html'
	success_url = reverse_lazy('categoria:categoria_listar')


class CategoriaDelete(DeleteView):
	model = Categoria
	template_name = 'categoria/categoria_delete.html'
	success_url = reverse_lazy('categoria:categoria_listar')
