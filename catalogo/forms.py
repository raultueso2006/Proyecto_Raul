from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["tipo", "nombre", "imagen"]
        labels = {
            "tipo": "Seleccionar tipo",
            "nombre": "Nombre",
            "imagen": "Agregar imagen",
        }
