from django.conf import settings
from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    # Registro interno del negocio: solo lo ve el personal autorizado (staff).
    costo_interno = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # Dueño del registro. Lo asigna el servidor, nunca el formulario.
    propietario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="productos",
        null=True,
        blank=True,
        editable=False,
    )

    def __str__(self):
        return self.nombre
