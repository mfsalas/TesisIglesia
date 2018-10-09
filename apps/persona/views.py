from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.persona.forms import PersonaForm, MatrimonioForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from apps.persona.models import Persona, Matrimonio


# Persona
def index(request):
    return render(request, 'persona/index.html')


def persona_view(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('persona:persona_listar')
    else:
        form = PersonaForm
    return render(request, 'persona/persona_form.html', {'form':form})


def persona_list(request):
	persona = Persona.objects.all().order_by('id')
	contexto = {'persona':persona}
	return render(request, 'persona/persona_list.html', contexto)

def persona_edit(request, id_persona):
    persona = Persona.objects.get(id=id_persona)
    if request.method == 'GET':
        form = PersonaForm(instance=persona)
    else:
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('persona:persona_listar')
    return render(request,'persona/persona_form.html',{'form':form})

def persona_delete(request, id_persona):
    persona = Persona.objects.get(id=id_persona)
    if request.method == 'POST':
        persona.delete()
        return redirect('persona:persona_listar')
    return render(request,'persona/persona_delete.html',{'persona':persona})




class PersonaList(ListView):
	model = Persona
	template_name = 'persona/persona_list.html'
	paginate_by = 3

class PersonaCreate(CreateView):
	model = Persona
	form_class = PersonaForm
	template_name = 'persona/persona_form.html'
	success_url = reverse_lazy('persona:persona_listar')

class PersonaUpdate(UpdateView):
	model = Persona
	form_class = PersonaForm
	template_name = 'persona/persona_form.html'
	success_url = reverse_lazy('persona:persona_listar')


class PersonaDelete(DeleteView):
	model = Persona
	template_name = 'persona/persona_delete.html'
	success_url = reverse_lazy('persona:persona_listar')

#Matrimonio
def matrimonio_view(request):
    if request.method == 'POST':
        form = MatrimonioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('matrimonio:matrimonio_listar')
    else:
        form = MatrimonioForm
    return render(request, 'matrimonio/matrimonio_form.html', {'form':form})


def matrimonio_list(request):
	matrimonio = Matrimonio.objects.all().order_by('id')
	contexto = {'matrimonio':matrimonio}
	return render(request, 'matrimonio/matrimonio_list.html', contexto)

def matrimonio_edit(request, id_matrimonio):
    matrimonio = Matrimonio.objects.get(id=id_matrimonio)
    if request.method == 'GET':
        form = MatrimonioForm(instance=matrimonio)
    else:
        form = MatrimonioForm(request.POST, instance=matrimonio)
        if form.is_valid():
            form.save()
            return redirect('matrimonio:matrimonio_listar')
    return render(request,'matrimonio/matrimonio_form.html',{'form':form})

def matrimonio_delete(request, id_matrimonio):
    matrimonio = Matrimonio.objects.get(id=id_matrimonio)
    if request.method == 'POST':
        matrimonio.delete()
        return redirect('matrimonio:matrimonio_listar')
    return render(request,'matrimonio/matrimonio_delete.html',{'matrimonio':matrimonio})




class MatrimonioList(ListView):
	model = Matrimonio
	template_name = 'matrimonio/matrimonio_list.html'
	paginate_by = 3

class MatrimonioCreate(CreateView):
	model = Matrimonio
	form_class = MatrimonioForm
	template_name = 'matrimonio/matrimonio_modal.html'
	success_url = None

class MatrimonioUpdate(UpdateView):
	model = Matrimonio
	form_class = MatrimonioForm
	template_name = 'matrimonio/matrimonio_form.html'
	success_url = reverse_lazy('matrimonio:matrimonio_listar')


class MatrimonioDelete(DeleteView):
	model = Matrimonio
	template_name = 'matrimonio/matrimonio_delete.html'
	success_url = reverse_lazy('matrimonio:matrimonio_listar')
