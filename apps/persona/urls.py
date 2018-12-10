from django.conf.urls import include, url
from apps.persona import views
from django.contrib.auth.decorators import login_required
from apps.persona.views import index, persona_view, persona_list, persona_list_baja, persona_restore, persona_edit, persona_delete, \
MatrimonioList, MatrimonioCreate, MatrimonioUpdate, MatrimonioDelete, matrimonio_view, matrimonio_list, matrimonio_edit, matrimonio_delete


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$',views.persona_view, name='persona_crear'),
    url(r'^listar$', views.persona_list, name='persona_listar'),
    url(r'^listar/baja/$', views.persona_list_baja, name='persona_listar_baja'),
    url(r'^editar/(?P<pk>\d+)/$', views.persona_edit, name='persona_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', views.persona_delete, name='persona_eliminar'),
    url(r'^restaurar/(?P<pk>\d+)/$', views.persona_restore, name='persona_restaurar'),
    url(r'^nuevo_matrimonio$',login_required(MatrimonioCreate.as_view()), name='matrimonio_crear'),
    url(r'^listar_matrimonio$', login_required(MatrimonioList.as_view()), name='matrimonio_listar'),
    url(r'^editar_matrimonio/(?P<pk>\d+)/$', login_required(MatrimonioUpdate.as_view()), name='matrimonio_editar'),
    url(r'^eliminar_matrimonio/(?P<pk>\d+)/$', login_required(MatrimonioDelete.as_view()), name='matrimonio_eliminar'),
]
