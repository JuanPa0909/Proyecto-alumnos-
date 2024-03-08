from django.db import models
from datetime import date

class Alumno(models.Model):
    carnet = models.CharField(max_length=10)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo_electronico = models.EmailField()
    fecha_nacimiento = models.DateField()

    def edad(self):
        today = date.today()
        age = today.year - self.fecha_nacimiento.year - ((today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
        return age
