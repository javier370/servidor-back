from django.db import models

from paciente.models import Paciente
from consultorio.models import Consultorio
from user.models import User

class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    consultorio = models.ForeignKey(Consultorio, on_delete=models.CASCADE)
    practicante = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    estado = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        db_table = 'cita'

    def __str__(self):
        return f'{self.paciente} - {self.practicante} - {self.consultorio} - {self.fecha}'
