from rest_framework.viewsets import ModelViewSet
from cita.models import Cita
from rest_framework.permissions import IsAuthenticated
from cita.api.serializers import CitaSerializer

class CitaApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CitaSerializer
    queryset = Cita.objects.all()