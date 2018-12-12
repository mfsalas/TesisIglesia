from django import forms

from apps.celula.models import Celula

class CelulaForm(forms.ModelForm):

    class Meta:
        model = Celula

        fields = [
            'dia_celula',
            'hora_celula',
            'direccion_celula',
        ]
        labels = {
            'dia_celula': 'Dia de la célula',
            'hora_celula': 'Horario de la célula',
            'direccion_celula': 'Dirección de la célula',
        }
