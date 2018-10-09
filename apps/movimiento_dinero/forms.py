from django import forms

from apps.movimiento_dinero.models import Movimiento_Dinero, Categoria

class Movimiento_DineroForm(forms.ModelForm):

    class Meta:
        model = Movimiento_Dinero

        fields = [
            'fecha_movimiento',
            'tipo_movimiento',
            'clase_movimiento',
            'monto_movimiento',
            'id_categoria',
            'descripcion_movimiento',
            'id_persona',
            'id_evento',
            'id_matrimonio',
            'id_ministerio',
        ]
        labels = {
            'fecha_movimiento': 'Fecha Movimiento',
            'tipo_movimiento': 'Tipo de Movimiento',
            'clase_movimiento': 'Clase de Movimiento',
            'monto_movimiento': 'Monto',
            'id_categoria': 'Categoria',
            'descripcion_movimiento': 'Descripcion',
            'id_persona': 'Autor',
            'id_evento': 'Evento',
            'id_matrimonio': 'Matrimonio',
            'id_ministerio': 'Ministerio',
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = [
                'nombre_categoria'
        ]
        labels = {
                'nombre_categoria':'Nombre Categoria'
        }
