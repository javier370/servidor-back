from django.db import models

class Paciente(models.Model):
    nombres = models.CharField(max_length=50, null=False, blank=False)
    apellidos = models.CharField(max_length=50, null=False, blank=False)
    fecha_nac = models.DateField(null=False, blank=False)
    documento = models.IntegerField(null=False, blank=False)
    genero = models.CharField(max_length=50, null=True, blank=True)
    telefono = models.BigIntegerField(null=True, blank=True)
    zona_residencial = models.CharField(max_length=50)
    estado_civil = models.CharField(max_length=50)
    rh = models.CharField(max_length=3)
    credo = models.CharField(max_length=50)

    class Meta:
        db_table = 'paciente'

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'
