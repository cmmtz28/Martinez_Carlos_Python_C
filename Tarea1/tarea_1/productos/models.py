from django.db import models

# Create your models here.
class Productos(models.Model):

    class Meta:
        verbose_name = 'Productos'
        verbose_name_plural = 'Productos'
    nombre = models.CharField('Nombre del producto', max_length=300, default='Sin nombre')
    descripcion = models.CharField('Descripción del producto', max_length=300, default='Sin descripción')
    precio = models.IntegerField('Precio', blank=False)
    fecha = models.DateField('Fecha de registro', blank=False)
    estatus = models.BooleanField('Estatus',default=False)

def _str_(self):
    return self.nombre