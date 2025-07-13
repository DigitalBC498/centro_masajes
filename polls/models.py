from django.db import models



# Create your models here.

class Turno(models.Model):
  nombre= models.CharField(max_length=100)
  email= models.EmailField()
  telefono = models.CharField(max_length=20) 
  fecha = models.DateField()
  hora = models.TimeField()
  tipo = models.CharField(max_length=100) 
  tipo_masaje = models.CharField(max_length=100, choices=[('relajante', 'Masaje Relajante'),('descontracturante', 'Masaje Descontracturante'),('facial', 'Masaje Facial'),
])
  
cancelado=models.BooleanField(default=False)

def __str__(self):
  return f"{self.nombre}" - {self.tipo_masaje} -{self.fecha} -{self.hora}


        
