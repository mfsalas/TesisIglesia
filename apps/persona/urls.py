from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from apps.persona.views import PersonaCreate,PersonaList,PersonaUpdate,PersonaDelete,index, persona_view, persona_list, persona_edit, persona_delete, \
MatrimonioList, MatrimonioCreate, MatrimonioUpdate, MatrimonioDelete, matrimonio_view, matrimonio_list, matrimonio_edit, matrimonio_delete


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$',login_required(PersonaCreate.as_view()), name='persona_crear'),
    url(r'^listar$', login_required(PersonaList.as_view()), name='persona_listar'),
    url(r'^editar/(?P<pk>\d+)/$', login_required(PersonaUpdate.as_view()), name='persona_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(PersonaDelete.as_view()), name='persona_eliminar'),
    url(r'^nuevo_matrimonio$',login_required(MatrimonioCreate.as_view()), name='matrimonio_crear'),
    url(r'^listar_matrimonio$', login_required(MatrimonioList.as_view()), name='matrimonio_listar'),
    url(r'^editar_matrimonio/(?P<pk>\d+)/$', login_required(MatrimonioUpdate.as_view()), name='matrimonio_editar'),
    url(r'^eliminar_matrimonio/(?P<pk>\d+)/$', login_required(MatrimonioDelete.as_view()), name='matrimonio_eliminar'),
]
