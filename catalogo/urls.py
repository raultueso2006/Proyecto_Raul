from django.urls import path
from . import views

urlpatterns = [
    path("", views.catalogo, name="catalogo"),
    path("agregar/", views.agregar_item, name="agregar_item"),
    path("marcar/<int:item_id>/", views.marcar_visto, name="marcar_visto"),
]