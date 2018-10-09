from django.conf.urls import url
from django.contrib.auth.views import login_required

from apps.ministerio.views import index_ministerio, MinisterioList, MinisterioCreate, MinisterioUpdate, \
	MinisterioDelete, ministerio_view, ministerio_list, ministerio_edit, ministerio_delete

urlpatterns = [
    url(r'^index$', index_ministerio),
    url(r'^ministerio/listar$', login_required(MinisterioList.as_view()), name='ministerio_listar'),
    url(r'^ministerio/nueva$', login_required(MinisterioCreate.as_view()), name='ministerio_crear'),
    url(r'^ministerio/editar/(?P<pk>\d+)$', login_required(MinisterioUpdate.as_view()), name='ministerio_editar'),
    url(r'^ministerio/eliminar/(?P<pk>\d+)$', login_required(MinisterioDelete.as_view()), name='ministerio_eliminar'),

]
