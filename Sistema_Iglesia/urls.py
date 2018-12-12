"""Sistema_Iglesia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from apps.persona import views
from apps.ministerio import views
from apps.usuario import views
from apps.evento import views
from django.contrib.auth.views import login, logout_then_login, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from apps.usuario.views import RegistroUsuario

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^persona/', include('apps.persona.urls', namespace='persona')),
    url(r'^matrimonio/', include('apps.persona.urls', namespace='matrimonio')),
    url(r'^movimiento/', include('apps.movimiento_dinero.urls', namespace='movimiento')),
    url(r'^categoria/', include('apps.movimiento_dinero.urls', namespace='categoria')),
    url(r'^ministerio/', include('apps.ministerio.urls', namespace='ministerio')),
    url(r'^evento/', include('apps.evento.urls', namespace='evento')),
    url(r'^articulo/', include('apps.inventario.urls', namespace='articulo')),
    url(r'^unidad_de_medida/', include('apps.inventario.urls', namespace='unidad_de_medida')),
    url(r'^entrada/', include('apps.entrada.urls', namespace='entrada')),
    url(r'^salida/', include('apps.salida.urls', namespace='salida')),
    url(r'^usuario/', include('apps.usuario.urls', namespace='usuario')),
    url(r'^accounts/login/', login, {'template_name':'index.html'}, name='login'),
    url(r'^logout/', logout_then_login, name='logout'),
    #url(r'^password/recovery/',
	#	RegistroUsuario.as_view(
	#		template_name='restration/password_reset_form.html',
	#		email_template_name='restration/password_reset_email.html',
	#	),
	#	name='password_reset',
	#	),
    url(r'^reset/password_reset', password_reset,
        {'template_name':'registration/password_reset_form.html',
        'email_template_name': 'registration/password_reset_email.html'},
        name='password_reset'),

    url(r'^password_reset_done', password_reset_done,
        {'template_name': 'registration/password_reset_done.html'},
        name='password_reset_done'),

    url(r'^password/recovery/(?P<uidb64>[0-9A-Za-z_\-]+)/'
        r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm,
        {'template_name': 'registration/password_reset_confirm.html'},
        name='password_reset_confirm'
        ),

    # url(
    #    r'^password/recovery/(?P<uidb64>[0-9A-Za-z_\-]+)/'
    #    r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #    auth_views.PasswordResetConfirmView.as_view(
    #        success_url=reverse_lazy('home'),
    #        post_reset_login=True,
    #        template_name='registration/password_reset_confirm.html',
    #        post_reset_login_backend=(
    #            'django.contrib.auth.backends.AllowAllUsersModelBackend'
    #        ),
    #    ),
    #    name='password_reset_confirm',
    #),

    url(r'^reset/done', password_reset_complete, {'template_name': 'registration/password_reset_complete.html'},
        name='password_reset_complete'),



]
