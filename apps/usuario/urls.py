from django.conf.urls import patterns, include, url
from .views import RegistroUsuario

urlpatterns = [

	url(r'^$' , 'django.contrib.auth.views.login',
		{'template_name':'persona/index.html'}, name='login'),

	url(r'^cerrar/$' , 'django.contrib.auth.views.logout_then_login',
		 name='logout'),

	url(r'^registrarse/$', RegistroUsuario.as_view() , name ='registrarse'),

	
]
