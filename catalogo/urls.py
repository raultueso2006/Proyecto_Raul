from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo, name='catalogo'),               # Página principal del catálogo
    path('agregar/', views.agregar_item, name='agregar_item'),
    path('marcar/<int:item_id>/', views.marcar_visto, name='marcar_visto'),
    path('eliminar/<int:item_id>/', views.eliminar_item, name='eliminar_item'),  # 🗑️ Nueva ruta
]