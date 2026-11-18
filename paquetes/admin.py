from django.contrib import admin

from .models import Categoria, Paquete


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "descripcion")
    search_fields = ("nombre",)


@admin.register(Paquete)
class PaqueteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "destino", "categoria", "precio", "fecha_salida", "cupos", "disponible")
    list_filter = ("categoria", "disponible", "fecha_salida")
    search_fields = ("nombre", "destino")
