from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Producto
# Create your views here.

def index(request):
    productos = Producto.objects.all()
    # productos = Producto.objects.filter(puntaje = 3)
    # productos = Producto.objects.get(pk=1)
    return render (
        request,
        'index.html',
        context={'productos': productos}
    )