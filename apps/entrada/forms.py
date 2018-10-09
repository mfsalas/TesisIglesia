from django import forms

from apps.entrada.models import Entrada

class EntradaForm(forms.ModelForm):

    class Meta:
        model = Entrada

        fields = [
            'id_articulo',
            'id_ministerio',
            'cantidad_entrada',
            'fecha_entrada',
            'observaciones_entrada',
        ]
        labels = {
            'id_articulo': 'Articulo',
            'id_ministerio': 'Ministerio',
            'cantidad_entrada': 'Cantidad de Entradas',
            'fecha_entrada': 'Fecha de Entrada',
            'observaciones_entrada': 'Observaciones',
        }
