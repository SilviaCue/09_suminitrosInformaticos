from django.db import models
from django.contrib.auth import get_user_model
from tienda.models import Tienda
from django.db.models import F, Sum, FloatField

# Create your models here.

User = get_user_model()


class Pedido(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    @property
    def total(self):
        return self.lineapedido_set.aggregate(
            total=Sum(F("precio")* F("cantidad"), output_field=FloatField())
        )["total"]

    class Meta:
        db_table = 'pedidos'
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
        ordering = ["id"]


class LineaPedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto_id = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    pedido_id = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} unidades de {}".format(self.cantidad, self.producto_id.producto)

    class Meta:
        db_table = 'lineaPedidos'
        verbose_name = 'Linea Pedido'
        verbose_name_plural = 'Linea Pedidos'
        ordering = ["id"]
