from rest_framework import serializers
from cita.models import Cita

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = ['id', 'paciente', 'practicante', 'consultorio', 'fecha', 'estado']