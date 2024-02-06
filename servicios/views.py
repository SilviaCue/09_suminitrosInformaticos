from django.shortcuts import render
from servicios.models import Servicio

# Create your views here.


def inventario(request):
    servicios = Servicio.objects.all()
    return render(request, "servicios/servicios.html", {"servicios": servicios})
