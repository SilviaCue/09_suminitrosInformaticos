from django.shortcuts import render
from .carro import Carro
from tienda.models import Tienda
from django.shortcuts import redirect

# Create your views here.


def agregar_producto(request, tienda_id):
    carro = Carro(request)
    tienda = Tienda.objects.get(id=tienda_id)
    carro.agregar(tienda=tienda)
    return redirect("Tienda")


def eliminar_producto(request, tienda_id):
    carro = Carro(request)
    tienda = Tienda.objects.get(id=tienda_id)
    carro.eliminar(tienda=tienda)
    return redirect("Tienda")


def restar_producto(request, tienda_id):
    carro = Carro(request)
    tienda = Tienda.objects.get(id=tienda_id)
    carro.restar_producto(tienda=tienda)
    return redirect("Tienda")


def limpiar_carro(request, tienda_id):
    carro = Carro(request)
    carro.limpiar_carro
    return redirect("Tienda")
