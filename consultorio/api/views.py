from rest_framework.viewsets import ModelViewSet
from consultorio.models import Consultorio
from rest_framework.permissions import IsAuthenticated
from consultorio.api.serializers import ConsultorioSerializer

class ConsultorioApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ConsultorioSerializer
    queryset = Consultorio.objects.all()
    