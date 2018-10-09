from django import forms

from apps.inventario.models import Unidadad_de_Medida, Articulo

class ArticuloForm(forms.ModelForm):

    class Meta:
        model = Articulo

        fields = [
            'descripcion_articulo',
            'cantidad_articulo',
            'id_unidad_de_medida',
            'precio_Compra_articulo',
        ]
        labels = {
            'descripcion_articulo': 'Descripcion Articulo',
            'cantidad_articulo': 'Cantidad',
            'precio_Compra_articulo': 'Precio Articulo',

        }

class Unidadad_de_MedidaForm(forms.ModelForm):
    class Meta:
        model = Unidadad_de_Medida
        fields = [
                'nombre_unidad'
        ]
        labels = {
                'nombre_unidad':'Nombre Unidad de Medida'
        }
