from django.db import models

class Item(models.Model):
    TYPE_CHOICES = (
        ('book', 'Libro'),
        ('movie', 'Película'),
    )

    title = models.CharField(max_length=255)
    short_description = models.TextField(blank=True)
    item_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)  # portadas en media/covers/
    genre = models.CharField(max_length=100, blank=True)
    popularity = models.IntegerField(default=0)  # para recomendaciones por popularidad

    def __str__(self):
        return f"{self.title} ({self.get_item_type_display()})"
