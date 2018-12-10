from django.conf.urls import include, url
from django.contrib.auth.views import login_required
from apps.ministerio import views
from apps.ministerio.views import index_ministerio, ministerio_view, ministerio_list, ministerio_edit, \
ministerio_delete, ministerio_list_baja, ministerio_restore

urlpatterns = [
    url(r'^index$', index_ministerio),
    url(r'^ministerio/nueva$', views.ministerio_view , name='ministerio_crear'),
    url(r'^ministerio/listar$', views.ministerio_list , name='ministerio_listar'),
    url(r'^ministerio/editar/(?P<pk>\d+)$', views.ministerio_edit , name='ministerio_editar'),
    url(r'^ministerio/eliminar/(?P<pk>\d+)$', views.ministerio_delete , name='ministerio_eliminar'),
	url(r'^ministerio/listar/baja/$', views.ministerio_list_baja , name='ministerio_listar_baja'),
	url(r'^ministerio/restaurar/(?P<pk>\d+)/$', views.ministerio_restore , name='ministerio_restaurar'),
]
