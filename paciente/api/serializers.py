from rest_framework import serializers
from paciente.models import Paciente

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['id', 'nombres', 'apellidos', 'fecha_nac', 'documento', 'genero', 'telefono', 'zona_residencial', 'estado_civil', 'rh', 'credo']