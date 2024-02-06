from django.shortcuts import render, HttpResponse
from carro.carro import Carro


# Create your views here.


def home(request):

    return render(request, "SuministrosInformaticosApp/home.html")


def datos(request):
    return render(request, "SuministrosInformaticosApp/datos.html")
