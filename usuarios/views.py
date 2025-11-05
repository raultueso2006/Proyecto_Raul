from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# 🔐 Iniciar sesión
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("catalogo")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    return render(request, "usuarios/login.html")

# 🚪 Cerrar sesión
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")
    else:
        # Evita el error 405 devolviendo a login si alguien entra por GET
        return redirect("login")

# 🧾 Crear cuenta
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya existe.")
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, "Cuenta creada correctamente. Ahora inicia sesión.")
            return redirect("login")
    return render(request, "usuarios/register.html")