from django.shortcuts import render, redirect
from .models import Producto, Categoria
from .categoria_form import CategoriaForm  # Importar el formulario correctamente
from django.contrib import messages
from .productosForm import ProductoForm  # Importa el formulario actualizado
from django.shortcuts import render, redirect, get_object_or_404

def index(request):
    return render(request, 'webapp/index.html')

def registrar_productos(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto guardado exitosamente.')
            return redirect('productos')  # Redirige a la misma página de productos
        else:
            messages.error(request, 'Ha ocurrido un error al guardar el producto.')
    else:
        form = ProductoForm()
    
    categorias = Categoria.objects.all()  # Asegúrate de tener las categorías disponibles para el formulario
    
    return render(request, 'webapp/productos.html', {
        'form': form,
        'categorias': categorias,
        'productos': Producto.objects.all()  # Esto es para mostrar los productos registrados
    })
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

def editar_categoria(request, id_categoria):
    categoria = get_object_or_404(Categoria, id_categoria=id_categoria)
    
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría actualizada correctamente.')
            return redirect('categorias')
        else:
            # Añadir un mensaje de error más detallado
            error_message = "Error al actualizar categoría: "
            for field in form:
                for error in field.errors:
                    error_message += f"{field.label}: {error} "
            messages.error(request, error_message)
    else:
        form = CategoriaForm(instance=categoria)
    
    return render(request, 'webapp/editar_categoria.html', {'form': form})


def registrar(request):
    return render(request, 'webapp/registrar.html')

def iniciar(request):
    return render(request, 'webapp/iniciar.html')


def eliminar_producto(request, id_producto):
    producto = get_object_or_404(Producto, id_producto=id_producto)
    producto.delete()
    messages.success(request, 'El producto se ha eliminado correctamente.')
    return redirect('productos')

def editar_producto(request, id_producto):
    # Obtener el producto a editar por su ID, si no existe retornar un 404
    producto = get_object_or_404(Producto, id_producto=id_producto)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'El producto se ha actualizado correctamente.')
            return redirect('productos')  # Redirige a la lista de productos después de la edición
    else:
        form = ProductoForm(instance=producto)
    
    return render(request, 'webapp/editar_producto.html', {'form': form})
