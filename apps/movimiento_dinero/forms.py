from django import forms

from apps.movimiento_dinero.models import Movimiento_Dinero, Categoria

class Movimiento_DineroForm(forms.ModelForm):

    class Meta:
        model = Movimiento_Dinero

        fields = [
            'fecha_movimiento',
            'clase_movimiento',
            'descripcion_movimiento',
            'monto_movimiento',
            'id_categoria',
#            'tipo_movimiento',
            'id_persona',
            'id_evento',
            'id_matrimonio',
            'id_ministerio',
        ]
        labels = {
            'fecha_movimiento': 'Fecha Movimiento',
            'clase_movimiento': 'Fijo/Eventual',
            'descripcion_movimiento': 'Descripcion',
            'monto_movimiento': 'Monto',
            'id_categoria': 'Categoria',
#            'tipo_movimiento' : "Tipo movimiento",
            'id_persona': 'Autor',
            'id_evento': 'Evento',
            'id_matrimonio': 'Matrimonio',
            'id_ministerio': 'Ministerio',
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = [
                'tipo_movimiento',
                'nombre_categoria'
        ]
        labels = {
                'tipo_movimiento': 'Ingreso/Egreso',
                'nombre_categoria':'Nombre Categoria',
        }
