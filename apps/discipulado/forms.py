from django import forms

from apps.discipulado.models import Discipulado, Discipulador

class DiscipuladosForm(forms.ModelForm):

    class Meta:
        model = Discipulado

        fields = [
            'nombre_material_discipulado',
            'discipulador',
            'persona',
            'fecha_fin',
        ]
        labels = {
            'nombre_material_discipulado': 'Nombre del material',
            'discipulador': 'Discipulador',
            'persona': 'Persona discipulada',
            'fecha_fin': 'Fecha fin discipulado',
        }

#class DiscipuladoresForm(forms.ModelForm):
                                                                                ######## no va asi jaja
#    class Meta:
#        model = Discipulador

#        fields = [
#            'id_discipulador',
#            'id_persona',
#        ]
#        labels = {
#            'id_discipulador': 'Discipulador',
#            'id_persona': 'Persona',

#        }
