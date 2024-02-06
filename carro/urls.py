from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "carro"

urlpatterns = [
    path("agregar/<int:tienda_id>/", views.agregar_producto, name="agregar"),
    path("eliminar/<int:tienda_id>/", views.eliminar_producto, name="eliminar"),
    path("restar/<int:tienda_id>/", views.restar_producto, name="restar"),
    path("limpiar/", views.limpiar_carro, name="limpiar"),
]
