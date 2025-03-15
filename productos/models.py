from django.db import models

# Modelo para Abarrotes
class Abarrotes(models.Model):
    # Campo para la imagen del producto
    imagen_abarrotes = models.ImageField(upload_to='abarrotes/', blank=True, null=True, verbose_name="Imagen del Producto")
    
    # Campo para el nombre del producto
    nombre_producto = models.CharField(max_length=255, verbose_name="Nombre del Producto")
    
    # Campo para el precio del producto
    precio_producto = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio del Producto")
    
    # Campo opcional para la descripción del producto
    descripcion_producto = models.TextField(blank=True, null=True, verbose_name="Descripción del Producto")

    def __str__(self):
        return self.nombre_producto

    class Meta:
        verbose_name = "Abarrote"
        verbose_name_plural = "Abarrotes"

# Modelo para Pastillas
class Pastillas(models.Model):
    # Campo para la imagen del producto
    imagen_pastillas = models.ImageField(upload_to='pastillas/', blank=True, null=True, verbose_name="Imagen del Producto")
    
    # Campo para el nombre del producto
    nombre_pastillas = models.CharField(max_length=255, verbose_name="Nombre del Producto")
    
    # Campo para el precio del producto
    precio_pastillas = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio del Producto")
    
    # Campo opcional para la descripción del producto
    descripcion_pastillas = models.TextField(blank=True, null=True, verbose_name="Descripción del Producto")

    def __str__(self):
        return self.nombre_pastillas

    class Meta:
        verbose_name = "Pastilla"
        verbose_name_plural = "Pastillas"