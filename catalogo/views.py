from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Item
from .forms import ItemForm

# 🔍 Vista principal del catálogo
@login_required
def catalogo(request):
    query = request.GET.get("q")
    items = Item.objects.filter(usuario=request.user).order_by("-creado")

    if query:
        items = items.filter(Q(nombre__icontains=query) | Q(tipo__icontains=query))

    return render(request, "catalogo/catalogo.html", {"items": items})

# ➕ Agregar nueva película, serie o libro
@login_required
def agregar_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.usuario = request.user
            item.save()
            return redirect("catalogo")
    else:
        form = ItemForm()

    return render(request, "catalogo/agregar_item.html", {"form": form})

# ✅ Marcar como visto / no visto
@login_required
def marcar_visto(request, item_id):
    item = get_object_or_404(Item, id=item_id, usuario=request.user)
    item.visto = not item.visto
    item.save()
    return redirect("catalogo")