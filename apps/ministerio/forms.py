from django import forms

from apps.ministerio.models import Ministerios

class MinisteriosForm(forms.ModelForm):

    class Meta:
        model = Ministerios

        fields = [
            'nombre_ministerio',
            'dia_actividad',
            'lugar_actividad',
            'hora_actividad',
        ]
        labels = {
            'nombre_ministerio': 'Nombre de Ministerio',
            'dia_actividad': 'Dia de la actividad',
            'lugar_actividad ': 'Lugar de la actividad',
            'hora_actividad': 'Hora de la actividad',
        }
