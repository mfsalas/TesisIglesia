from django.conf.urls import url
from django.contrib.auth.views import login_required

from apps.entrada.views import index_entrada, EntradaList, EntradaCreate, EntradaUpdate, \
	EntradaDelete, entrada_view, entrada_list, entrada_edit, entrada_delete
urlpatterns = [
    url(r'^index$', index_entrada),
    url(r'^entrada/listar$', login_required(EntradaList.as_view()), name='entrada_listar'),
    url(r'^entrada/nueva$', login_required(EntradaCreate.as_view()), name='entrada_crear'),
    url(r'^entrada/editar/(?P<pk>\d+)$', login_required(EntradaUpdate.as_view()), name='entrada_editar'),
    url(r'^entrada/eliminar/(?P<pk>\d+)$', login_required(EntradaDelete.as_view()), name='entrada_eliminar'),


]
