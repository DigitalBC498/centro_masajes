from django.db import models



# Create your models here.

class Turno(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    fecha = models.DateField()
    hora = models.TimeField()
    tipo_masaje = models.CharField(
        max_length=100,
        choices=[
            ('relajante', 'Masaje_Relajante'),
            ('descontracturante', 'Masaje_Descontracturante'),
            ('facial', 'Masaje_Facial'),
        ]
    )
    cancelado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} - {self.tipo_masaje} - {self.fecha} - {self.hora}"



        
