from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from apps.ministerio.models import Ministerios
from apps.ministerio.forms import MinisteriosForm
from apps.persona.models import Persona

from .models import Ministerios

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
	ministerio = Ministerio.objects.all().order_by('id')
	contexto = {'ministerio':ministerio}
	return render(request, 'ministerio/ministerio_listar.html', contexto)

def ministerio_edit(request, id_ministerio):
    ministerio = Ministerio.objects.get(id=id_ministerio)
    if request.method == 'GET':
        form = MinisteriosForm(instance=ministerio)
    else:
        form = MinisteriosForm(request.POST, instance=ministerio)
        if form.is_valid():
            form.save()
            return redirect('ministerio:ministerio_listar')
    return render(request,'ministerio/ministerio_form.html',{'form':form})

def ministerio_delete(request, id_ministerio):
    ministerio = Ministerio.objects.get(id=id_ministerio)
    if request.method == 'POST':
        ministerio.delete()
        return redirect('ministerio:ministerio_listar')
    return render(request,'ministerio/ministerio_delete.html',{'ministerio':ministerio})




class MinisterioList(ListView):
	model = Ministerios
	template_name = 'ministerio/ministerio_listar.html'
	paginate_by = 3

class MinisterioCreate(CreateView):
	model = Ministerios
	template_name = 'ministerio/ministerio_form.html'
	form_class = MinisteriosForm
	success_url = reverse_lazy('ministerio:ministerio_listar')

class MinisterioUpdate(UpdateView):
	model = Ministerios
	second_model = Persona
	template_name = 'ministerio/ministerio_form.html'
	form_class = MinisteriosForm
	success_url = reverse_lazy('ministerio:ministerio_listar')


class MinisterioDelete(DeleteView):
	model = Ministerios
	template_name = 'ministerio/ministerio_delete.html'
	success_url = reverse_lazy('ministerio:ministerio_listar')

class BuscarView(TemplateView):
    def post(self, request, *args, **kwargs):
        buscar = request.POST['buscalo']
        ministerios = Ministerios.objects.filter(nombre_ministerio__contains=buscar)
        return render(request,'ministerio/buscar.html',
        {'ministerios':ministerios, 'min' : True})
