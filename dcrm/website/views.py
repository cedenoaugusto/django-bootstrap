from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        usuario = request.POST['txtNombre']
        clave = request.POST['txtContrasena']
        print(usuario, clave)

        user = authenticate(request, username=usuario, password=clave)

        if user is None:
            messages.warning(request, "Ingreso fallido")
        else:
            login(request, user)
            messages.success(request, "Ingreso correctamente")
            
        return redirect('home')

    return render(request, 'home.html', {})

# def login_user(request):


def logout_user(request):
    logout(request)
    messages.success(request, "Cerro la sesion correctamente")
    return redirect('home')


def registrar_usuario(request):
    return render(request, 'register.html', {})
