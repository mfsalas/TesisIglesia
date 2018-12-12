from django.conf.urls import url
from django.contrib.auth.views import login_required

from apps.inventario.views import index_articulo, ArticuloList, ArticuloCreate, ArticuloUpdate, \
	ArticuloDelete, articulo_view, articulo_list, articulo_edit, articulo_delete, \
	Unidadad_de_MedidaList, Unidadad_de_MedidaCreate, Unidadad_de_MedidaUpdate, Unidadad_de_MedidaDelete, unidad_de_medida_view, unidad_de_medida_list, unidad_de_medida_edit, unidad_de_medida_delete

urlpatterns = [
    url(r'^index$', index_articulo),
    url(r'^articulo/listar$', login_required(ArticuloList.as_view()), name='articulo_listar'),
    url(r'^articulo/nueva$', login_required(ArticuloCreate.as_view()), name='articulo_crear'),
    url(r'^articulo/editar/(?P<pk>\d+)$', login_required(ArticuloUpdate.as_view()), name='articulo_editar'),
    url(r'^articulo/eliminar/(?P<pk>\d+)$', login_required(ArticuloDelete.as_view()), name='articulo_eliminar'),
	url(r'^nuevo_unidad_de_medida$',login_required(Unidadad_de_MedidaCreate.as_view()), name='unidad_de_medida_crear'),
    url(r'^listar_unidad_de_medida$', login_required(Unidadad_de_MedidaList.as_view()), name='unidad_de_medida_listar'),
    url(r'^editar_unidad_de_medida/(?P<pk>\d+)/$', login_required(Unidadad_de_MedidaUpdate.as_view()), name='unidad_de_medida_editar'),
    url(r'^eliminar_unidad_de_medida/(?P<pk>\d+)/$', login_required(Unidadad_de_MedidaDelete.as_view()), name='unidad_de_medida_eliminar'),

]
