from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Lugar(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    direccion = models.CharField(max_length=200, blank=True)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, related_name='lugares'
    )

    def __str__(self):
        return self.nombre


class Resena(models.Model):
    lugar = models.ForeignKey(
        Lugar, on_delete=models.CASCADE, related_name='resenas'
    )
    autor = models.CharField(max_length=100)
    comentario = models.TextField()
    calificacion = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        return f'{self.autor} - {self.lugar}'