from django.contrib import admin
from .models import Abarrotes, Pastillas

# Configuración del administrador para Abarrotes
@admin.register(Abarrotes)
class AbarrotesAdmin(admin.ModelAdmin):
    # Usar los nuevos nombres de los campos
    list_display = ('nombre_producto', 'precio_producto', 'descripcion_producto')  # Campos que se mostrarán en la lista
    search_fields = ('nombre_producto',)  # Campo por el que se puede buscar
    list_filter = ('precio_producto',)  # Filtro por precio

# Configuración del administrador para Pastillas
@admin.register(Pastillas)
class PastillasAdmin(admin.ModelAdmin):
    # Usar los nuevos nombres de los campos
    list_display = ('nombre_pastillas', 'precio_pastillas', 'descripcion_pastillas')  # Campos que se mostrarán en la lista
    search_fields = ('nombre_pastillas',)  # Campo por el que se puede buscar
    list_filter = ('precio_pastillas',)  # Filtro por precio