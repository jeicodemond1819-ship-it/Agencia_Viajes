from django.db import models


class Categoria(models.Model):
    """Modelo PADRE clasificador (se gestiona solo desde Django Admin)."""

    nombre = models.CharField(max_length=80, unique=True)
    descripcion = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Categoría de viaje"
        verbose_name_plural = "Categorías de viaje"

    def __str__(self):
        return self.nombre


class Paquete(models.Model):
    """Modelo HIJO operativo (CRUD público con CBVs)."""

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="paquetes",
    )
    nombre = models.CharField(max_length=120)
    destino = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=0, help_text="Precio por persona en CLP")
    fecha_salida = models.DateField()
    cupos = models.PositiveIntegerField(default=10)
    disponible = models.BooleanField(default=True)

    class Meta:
        ordering = ["fecha_salida"]

    def __str__(self):
        return f"{self.nombre} - {self.destino}"
