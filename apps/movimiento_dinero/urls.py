from django.conf.urls import include, url
from apps.movimiento_dinero import views
from django.contrib.auth.views import login_required
from apps.movimiento_dinero.views import index_movimiento, movimiento_restore, movimiento_list_baja, movimiento_view, movimiento_list, movimiento_edit, movimiento_delete, \
CategoriaList, CategoriaCreate, CategoriaUpdate, CategoriaDelete, categoria_view, categoria_list, categoria_edit, categoria_delete

urlpatterns = [
    url(r'^index$', index_movimiento),
    url(r'^movimiento/listar$', views.movimiento_list , name='movimiento_listar'),
	url(r'^movimiento/listar/baja/$', views.movimiento_list_baja , name='movimiento_listar_baja'),
    url(r'^movimiento/nueva$', views.movimiento_view , name='movimiento_crear'),
    url(r'^movimiento/editar/(?P<pk>\d+)/$', views.movimiento_edit , name='movimiento_editar'),
    url(r'^movimiento/eliminar/(?P<pk>\d+)/$', views.movimiento_delete , name='movimiento_eliminar'),
	url(r'^movimiento/restaurar/(?P<pk>\d+)/$', views.movimiento_restore , name='movimiento_restaurar'),
	url(r'^nuevo_categoria$',login_required(CategoriaCreate.as_view()), name='categoria_crear'),
    url(r'^listar_categoria$', login_required(CategoriaList.as_view()), name='categoria_listar'),
    url(r'^editar_categoria/(?P<pk>\d+)/$', login_required(CategoriaUpdate.as_view()), name='categoria_editar'),
    url(r'^eliminar_categoria/(?P<pk>\d+)/$', login_required(CategoriaDelete.as_view()), name='categoria_eliminar'),

]
