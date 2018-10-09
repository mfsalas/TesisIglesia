from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.inventario.models import Unidadad_de_Medida, Articulo
from apps.inventario.forms import ArticuloForm, Unidadad_de_MedidaForm

from apps.persona.models import Persona


def index_articulo(request):
	return HttpResponse("soy la pagina principal de la app adopcion")

def articulo_view(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articulo:articulo_listar')
    else:
        form = ArticuloForm
    return render(request, 'articulo/articulo_form.html', {'form':form})

def articulo_list(request):
	articulo = Articulo.objects.all().order_by('id')
	contexto = {'articulo':articulo}
	return render(request, 'articulo/articulo_list.html', contexto)

def articulo_edit(request, id_articulo):
    articulo = Articulo.objects.get(id=id_articulo)
    if request.method == 'GET':
        form = ArticuloForm(instance=articulo)
    else:
        form = ArticuloForm(request.POST, instance=articulo)
        if form.is_valid():
            form.save()
            return redirect('articulo:articulo_listar')
    return render(request,'articulo/articulo_form.html',{'form':form})

def articulo_delete(request, id_articulo):
    articulo = Articulo.objects.get(id=id_articulo)
    if request.method == 'POST':
        articulo.delete()
        return redirect('articulo:articulo_listar')
    return render(request,'articulo/articulo_delete.html',{'articulo':articulo})




class ArticuloList(ListView):
	model = Articulo
	template_name = 'articulo/articulo_list.html'
	paginate_by = 3

class ArticuloCreate(CreateView):
	model = Articulo
	template_name = 'articulo/articulo_form.html'
	form_class = ArticuloForm
	success_url = reverse_lazy('articulo:articulo_listar')

class ArticuloUpdate(UpdateView):
	model = Articulo
	second_model = Persona
	template_name = 'articulo/articulo_form.html'
	form_class = ArticuloForm
	success_url = reverse_lazy('articulo:articulo_listar')


class ArticuloDelete(DeleteView):
	model = Articulo
	template_name = 'articulo/articulo_delete.html'
	success_url = reverse_lazy('articulo:articulo_listar')

#Categorias
def unidad_de_medida_view(request):
    if request.method == 'POST':
        form = Unidadad_de_MedidaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('unidad_de_medida:unidad_de_medida_listar')
    else:
        form = Unidadad_de_MedidaForm
    return render(request, 'unidad_de_medida/unidad_de_medida_form.html', {'form':form})


def unidad_de_medida_list(request):
	categoria = Unidadad_de_Medida.objects.all().order_by('id')
	contexto = {'unidad_de_medida':unidad_de_medida}
	return render(request, 'unidad_de_medida/unidad_de_medida_list.html', contexto)

def unidad_de_medida_edit(request, id_unidad_de_medida):
    unidad_de_medida = Unidadad_de_Medida.objects.get(id=id_unidad_de_medida)
    if request.method == 'GET':
        form = Unidadad_de_MedidaForm(instance=unidad_de_medida)
    else:
        form = Unidadad_de_MedidaForm(request.POST, instance=unidad_de_medida)
        if form.is_valid():
            form.save()
            return redirect('unidad_de_medida:unidad_de_medida_listar')
    return render(request,'unidad_de_medida/unidad_de_medida_form.html',{'form':form})

def unidad_de_medida_delete(request, id_categoria):
    unidad_de_medida = Unidadad_de_Medida.objects.get(id=id_unidad_de_medida)
    if request.method == 'POST':
        categoria.delete()
        return redirect('unidad_de_medida:unidad_de_medida_listar')
    return render(request,'unidad_de_medida/unidad_de_medida_delete.html',{'unidad_de_medida':unidad_de_medida})




class Unidadad_de_MedidaList(ListView):
	model = Unidadad_de_Medida
	template_name = 'unidad_de_medida/unidad_de_medida_list.html'
	paginate_by = 3

class Unidadad_de_MedidaCreate(CreateView):
	model = Unidadad_de_Medida
	form_class = Unidadad_de_MedidaForm
	template_name = 'unidad_de_medida/unidad_de_medida_form.html'
	success_url = reverse_lazy('unidad_de_medida:unidad_de_medida_listar')

class Unidadad_de_MedidaUpdate(UpdateView):
	model = Unidadad_de_Medida
	form_class = Unidadad_de_MedidaForm
	template_name = 'unidad_de_medida/unidad_de_medida_form.html'
	success_url = reverse_lazy('unidad_de_medida:unidad_de_medida_listar')


class Unidadad_de_MedidaDelete(DeleteView):
	model = Unidadad_de_Medida
	template_name = 'unidad_de_medida/unidad_de_medida_delete.html'
	success_url = reverse_lazy('unidad_de_medida:unidad_de_medida_listar')
