from django.conf.urls import url
from django.contrib.auth.views import login_required

from apps.discipulado.views import index_discipulado,DiscipuladoList, DiscipuladoCreate, DiscipuladoUpdate, \
	DiscipuladoDelete, discipulado_view, discipulado_list, discipulado_edit, discipulado_delete, BuscarView

urlpatterns = [
    url(r'^index$', index_discipulado),
    url(r'^discipulado/listar$', login_required(DiscipuladoList.as_view()), name='discipulado_listar'),
    url(r'^discipulado/nueva$', login_required(DiscipuladoCreate.as_view()), name='discipulado_crear'),
    url(r'^discipulado/editar/(?P<pk>\d+)$', login_required(DiscipuladoUpdate.as_view()), name='discipulado_editar'),
    url(r'^discipulado/eliminar/(?P<pk>\d+)$', login_required(DiscipuladoDelete.as_view()), name='discipulado_eliminar'),
    url(r'^buscar/$', BuscarView.as_view(),name='buscar'),

]
