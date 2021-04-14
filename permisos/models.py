from django.db import models

from empleados.models import Empleado


class Permiso(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)
    activo = models.BooleanField()
    empleado = models.ForeignKey(
        Empleado,
        related_name='permisos',
        on_delete=models.SET_NULL,
        null=True
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
