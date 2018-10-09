from django.contrib import admin

# Register your models here.
from apps.movimiento_dinero.models import Movimiento_Dinero, Categoria
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Movimiento_Dinero)
