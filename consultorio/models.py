from django.db import models

class Consultorio(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    descripcion = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        db_table = 'consultorio'
    
    def __str__(self):
        return f'{self.nombre} - {self.descripcion}'