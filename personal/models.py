from django.db import models


class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Cargo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Empleado(models.Model):

    ESTADOS = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]

    rut = models.CharField(
        max_length=12,
        unique=True
    )

    nombre = models.CharField(
        max_length=100
    )

    apellido = models.CharField(
        max_length=100
    )

    correo = models.EmailField()

    telefono = models.CharField(
        max_length=20
    )

    fecha_ingreso = models.DateField()

    cargo = models.ForeignKey(
        Cargo,
        on_delete=models.PROTECT
    )

    departamento = models.ForeignKey(
        Departamento,
        on_delete=models.PROTECT
    )

    estado = models.CharField(
        max_length=10,
        choices=ESTADOS,
        default='Activo'
    )

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

