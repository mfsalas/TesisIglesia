from django import forms

from apps.persona.models import Persona, Matrimonio

class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona

        fields = [
            'nombre',
            'apellido_persona',
            'fecha_nacimiento',
            'sexo',
            'celular',
            'direccion',
            'id_matrimonio',
            'localidad',
            'estado_civil',
            'profesion',
            'bautizado',
            'escuela_biblica',
            'encuentro',

        ]
        labels = {
            'nombre': 'Nombre',
            'apellido_persona': 'Apellido',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'sexo': 'Sexo',
            'celular': 'Celular',
            'direccion': 'Direccion',
            'id_matrimonio': 'Matrimonio',
            'localidad': 'Localidad',
            'estado_civil':'Estado civil',
            'profesion': 'Profesión',
            'bautizado': 'Bautizado',
            'escuela_biblica': 'Escuela bíblica',
            'encuentro': 'Encuentro',

        }

class MatrimonioForm(forms.ModelForm):
    class Meta:
        model = Matrimonio
        fields = [
                'apellido_matrimonio'
        ]
        labels = {
                'apellido_matrimonio':'Apellido Matrimonio'
        }
