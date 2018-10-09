from django import forms

from apps.salida.models import Salida

class SalidaForm(forms.ModelForm):

    class Meta:
        model = Salida

        fields = [
            'id_articulo',
            'id_ministerio',
            'cantidad_salida',
            'fecha_salida',
            'observaciones_salida',
        ]
        labels = {
            'id_articulo': 'Articulo',
            'id_ministerio': 'Ministerio',
            'cantidad_salida': 'Cantidad de Salidas',
            'fecha_salida': 'Fecha de Salidas',
            'observaciones_salida': 'Observaciones',
        }
