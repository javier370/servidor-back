from rest_framework.viewsets import ModelViewSet
from paciente.models import Paciente
from rest_framework.permissions import IsAuthenticated
from paciente.api.serializers import PacienteSerializer

class PacienteApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PacienteSerializer
    queryset = Paciente.objects.all()