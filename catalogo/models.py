from django.db import models
from django.contrib.auth.models import User

TIPOS = [
    ('Pelicula', 'Película'),
    ('Serie', 'Serie'),
    ('Libro', 'Libro'),
]

class Item(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    nombre = models.CharField(max_length=150)
    imagen = models.ImageField(upload_to='items/', blank=True, null=True)
    visto = models.BooleanField(default=False)  # 👈 NUEVO CAMPO
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo}: {self.nombre}"