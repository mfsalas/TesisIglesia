from django.conf.urls import url
from django.contrib.auth.views import login_required

from apps.evento.views import index_evento, EventoList, EventoCreate, EventoUpdate, \
	EventoDelete, evento_view, evento_list, evento_edit, evento_delete

urlpatterns = [
    url(r'^index$', index_evento),
    url(r'^evento/listar$', login_required(EventoList.as_view()), name='evento_listar'),
    url(r'^evento/nueva$', login_required(EventoCreate.as_view()), name='evento_crear'),
    url(r'^evento/editar/(?P<pk>\d+)$', login_required(EventoUpdate.as_view()), name='evento_editar'),
    url(r'^evento/eliminar/(?P<pk>\d+)$', login_required(EventoDelete.as_view()), name='evento_eliminar'),

]
