from django.db import models

# Create your models here.


class Tienda(models.Model):
    OPCIONES_CATEGORIA = [
        ('formacion', 'Formación'),
        ('reparacion', 'Reparación'),
        ('producto', 'Producto'),
    ]

    categoria = models.CharField(max_length=20, choices=OPCIONES_CATEGORIA)
    producto = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="tienda", null=True, blank=True)
    unidades = models.IntegerField()
    precio = models.FloatField()
    proveedor = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'tienda'
        verbose_name_plural = 'tiendas'

    def __str__(self):
        return "{} - {} - {}".format(self.categoria, self.producto, self.precio)
