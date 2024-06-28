from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Producto, Categoria
from .categoria_form import CategoriaForm
from .productosForm import ProductoForm
from .registro_usuario import RegistroUsuarioForm
from .login_usuario import LoginForm

def index(request):
    num_categorias = Categoria.objects.count()
    num_productos = Producto.objects.count()
    
    context = {
        'num_categorias': num_categorias,
        'num_productos': num_productos
    }
    return render(request, 'webapp/index.html', context)

def registrar_productos(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto guardado exitosamente.')
            return redirect('productos') 
        else:
            messages.error(request, 'Ha ocurrido un error al guardar el producto.')
    else:
        form = ProductoForm()
    
    categorias = Categoria.objects.all()  
    return render(request, 'webapp/productos.html', {
        'form': form,
        'categorias': categorias,
        'productos': Producto.objects.all() 
    })

def registrar_categorias(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría agregada con éxito.')
            return redirect('categorias')
        else:
        
            error_message = "Error al agregar categoría: "
            for field, errors in form.errors.items():
                for error in errors:
                    error_message += f"{field}: {error}. "
            messages.error(request, error_message)
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
         
            error_message = "Error al actualizar categoría: "
            for field in form:
                for error in field.errors:
                    error_message += f"{field.label}: {error} "
            messages.error(request, error_message)
    else:
        form = CategoriaForm(instance=categoria)
    
    return render(request, 'webapp/editar_categoria.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bienvenido, {username}. Has iniciado sesión correctamente.')
                return redirect('index')
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
        else:
            messages.error(request, 'Por favor corrige los errores.')
    else:
        form = LoginForm()
    
    return render(request, 'webapp/iniciar.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión correctamente.')
    return redirect('index')

def eliminar_producto(request, id_producto):
    producto = get_object_or_404(Producto, id_producto=id_producto)
    producto.delete()
    messages.success(request, 'El producto se ha eliminado correctamente.')
    return redirect('productos')

def editar_producto(request, id_producto):
    producto = get_object_or_404(Producto, id_producto=id_producto)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'El producto se ha actualizado correctamente.')
            return redirect('productos')
    else:
        form = ProductoForm(instance=producto)
    
    return render(request, 'webapp/editar_producto.html', {'form': form})

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Usuario {username} registrado correctamente.')
            return redirect('registrar')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'Error en el campo {field}: {error}')
    else:
        form = RegistroUsuarioForm()
    
    return render(request, 'webapp/registrar.html', {'form': form})
