from django.conf.urls import url
from django.contrib.auth.views import login_required

from apps.celula.views import index_celula, CelulaList, CelulaCreate, CelulaUpdate, \
	CelulaDelete, celula_view, celula_list, celula_edit, celula_delete

urlpatterns = [
    url(r'^index$', index_celula),
    url(r'^celula/listar$', login_required(CelulaList.as_view()), name='celula_listar'),
    url(r'^celula/nueva$', login_required(CelulaCreate.as_view()), name='celula_crear'),
    url(r'^celula/editar/(?P<pk>\d+)$', login_required(CelulaUpdate.as_view()), name='celula_editar'),
    url(r'^celula/eliminar/(?P<pk>\d+)$', login_required(CelulaDelete.as_view()), name='celula_eliminar'),

]
