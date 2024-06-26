from django.shortcuts import render, redirect
from .models import Producto, Categoria
from .categoria_form import CategoriaForm  # Importar el formulario correctamente
from django.contrib import messages

def index(request):
    return render(request, 'webapp/index.html')

def registrar_productos(request):
    productos = Producto.objects.all()
    context = {
        'productos': productos
    }
    return render(request, 'webapp/productos.html', context)

def registrar_categorias(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría agregada con éxito.')
            return redirect('categorias')
        else:
            messages.error(request, 'Error al agregar categoría.')
    else:
        form = CategoriaForm()

    categorias = Categoria.objects.all()
    context = {
        'categorias': categorias,
        'form': form
    }
    return render(request, 'webapp/categorias.html', context)
def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id_categoria=id)
    if request.method == 'POST':
        categoria.delete()
        messages.success(request, 'Categoría eliminada correctamente.')
    return redirect('categorias')

def registrar(request):
    return render(request, 'webapp/registrar.html')

def iniciar(request):
    return render(request, 'webapp/iniciar.html')
