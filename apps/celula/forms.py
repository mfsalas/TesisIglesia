from django import forms

from apps.celula.models import Celula, Miembros_celula

class CelulaForm(forms.ModelForm):

    class Meta:
        model = Celula

        fields = [
            'dia_celula',
            'hora_celula',
            'direccion_celula',
            'encargado_celula',
        ]
        labels = {
            'dia_celula': 'Dia de la célula',
            'hora_celula': 'Horario de la célula',
            'direccion_celula': 'Dirección de la célula',
            'encargado_celula': 'Encargado',
        }

class MiembrosCelulaForm(forms.ModelForm):

    class Meta:
        model = Miembros_celula

        fields = [
            'miembro',
            #'rol',
        ]
        labels = {
            'miembro': 'Miembro',
        #    'rol': 'Rol',

        }
