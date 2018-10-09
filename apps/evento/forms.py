from django import forms

from apps.evento.models import Evento

class EventoForm(forms.ModelForm):

    class Meta:
        model = Evento

        fields = [
            'descripcion_evento',
            'fecha_evento',
            'lugar_evento',
            'hora_evento',
            #'id_ministerio_encargado'
        ]
        labels = {
            'descripcion_evento': 'Descripcion del evento',    #evento queda mejor que actividad especial
            'fecha_evento': 'Dia del evento',
            'lugar_evento': 'Lugar del evento',
            'hora_evento': 'Hora del evento',
        }
