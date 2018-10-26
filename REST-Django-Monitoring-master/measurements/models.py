from django.db import models

# Create your models here.
class Measurement(models.Model):
    Arrendatario = models.CharField(max_length=50)
    Precio = models.FloatField(null=True, blank=True, default=None)
    unit = models.CharField(max_length=50)
    Parqueadero = models.CharField(max_length=50)
    Hora llegada = models.TimeField(auto_now_add=False)
    Hora salida = models.TimeField(auto_now_add=False)
