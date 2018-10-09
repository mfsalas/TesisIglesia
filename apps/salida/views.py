from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.salida.models import Salida
from apps.salida.forms import SalidaForm

from apps.persona.models import Persona


def index_salida(request):
	return HttpResponse("soy la pagina principal de la app adopcion")

def salida_view(request):
    if request.method == 'POST':
        form = SalidaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('salida:salida_listar')
    else:
        form = SalidaForm
    return render(request, 'salida/salida_form.html', {'form':form})

def salida_list(request):
	salida = Salida.objects.all().order_by('id')
	contexto = {'salida':salida}
	return render(request, 'salida/salida_list.html', contexto)

def salida_edit(request, id_salida):
    salida = Salida.objects.get(id=id_salida)
    if request.method == 'GET':
        form = SalidaForm(instance=salida)
    else:
        form = SalidaForm(request.POST, instance=salida)
        if form.is_valid():
            form.save()
            return redirect('salida:salida_listar')
    return render(request,'salida/salida_form.html',{'form':form})

def salida_delete(request, id_salida):
    salida = Salida.objects.get(id=id_salida)
    if request.method == 'POST':
        salida.delete()
        return redirect('salida:salida_listar')
    return render(request,'salida/salida_delete.html',{'salida':salida})




class SalidaList(ListView):
	model = Salida
	template_name = 'salida/salida_list.html'
	paginate_by = 3

class SalidaCreate(CreateView):
	model = Salida
	template_name = 'salida/salida_form.html'
	form_class = SalidaForm
	success_url = reverse_lazy('salida:salida_listar')

class SalidaUpdate(UpdateView):
	model = Salida
	second_model = Persona
	template_name = 'salida/salida_form.html'
	form_class = SalidaForm
	success_url = reverse_lazy('salida:salida_listar')


class SalidaDelete(DeleteView):
	model = Salida
	template_name = 'salida/salida_delete.html'
	success_url = reverse_lazy('salida:salida_listar')
