# webapp/views.py
from django.shortcuts import render
from .models import Producto, Categoria  # Importa los modelos Producto y Categoria

def index(request):
    return render(request, 'webapp/index.html')

def productos(request):
    # Consulta todos los productos desde la base de datos
    productos = Producto.objects.all()
    context = {
        'productos': productos
    }
    return render(request, 'webapp/productos.html', context)

def categorias(request):
    # Consulta todas las categorías desde la base de datos
    categorias = Categoria.objects.all()
    context = {
        'categorias': categorias
    }
    return render(request, 'webapp/categorias.html', context)

def registrar(request):
    # Lógica para la página de registro
    return render(request, 'webapp/registrar.html')

def iniciar(request):
    # Lógica para la vista de iniciar sesión
    return render(request, 'webapp/iniciar.html')

