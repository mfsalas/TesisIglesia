from django.conf.urls import url
from django.contrib.auth.views import login_required

from apps.movimiento_dinero.views import index_movimiento, MovimientoList, MovimientoCreate, MovimientoUpdate, \
	MovimientoDelete, movimiento_view, movimiento_list, movimiento_edit, movimiento_delete, \
	CategoriaList, CategoriaCreate, CategoriaUpdate, CategoriaDelete, categoria_view, categoria_list, categoria_edit, categoria_delete

urlpatterns = [
    url(r'^index$', index_movimiento),
    url(r'^movimiento/listar$', login_required(MovimientoList.as_view()), name='movimiento_listar'),
    url(r'^movimiento/nueva$', login_required(MovimientoCreate.as_view()), name='movimiento_crear'),
    url(r'^movimiento/editar/(?P<pk>\d+)$', login_required(MovimientoUpdate.as_view()), name='movimiento_editar'),
    url(r'^movimiento/eliminar/(?P<pk>\d+)$', login_required(MovimientoDelete.as_view()), name='movimiento_eliminar'),
	url(r'^nuevo_categoria$',login_required(CategoriaCreate.as_view()), name='categoria_crear'),
    url(r'^listar_categoria$', login_required(CategoriaList.as_view()), name='categoria_listar'),
    url(r'^editar_categoria/(?P<pk>\d+)/$', login_required(CategoriaUpdate.as_view()), name='categoria_editar'),
    url(r'^eliminar_categoria/(?P<pk>\d+)/$', login_required(CategoriaDelete.as_view()), name='categoria_eliminar'),

]
