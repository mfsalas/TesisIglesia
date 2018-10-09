from django.conf.urls import url
from django.contrib.auth.views import login_required

from apps.salida.views import index_salida, SalidaList, SalidaCreate, SalidaUpdate, \
	SalidaDelete, salida_view, salida_list, salida_edit, salida_delete
urlpatterns = [
    url(r'^index$', index_salida),
    url(r'^salida/listar$', login_required(SalidaList.as_view()), name='salida_listar'),
    url(r'^salida/nueva$', login_required(SalidaCreate.as_view()), name='salida_crear'),
    url(r'^salida/editar/(?P<pk>\d+)$', login_required(SalidaUpdate.as_view()), name='salida_editar'),
    url(r'^salida/eliminar/(?P<pk>\d+)$', login_required(SalidaDelete.as_view()), name='salida_eliminar'),


]
