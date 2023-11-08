from django.urls import path
from rest_framework.routers import DefaultRouter

from paciente.api.views import PacienteApiViewSet

router_pacientes = DefaultRouter()
router_pacientes.register(prefix='pacientes', basename='pacientes', viewset=PacienteApiViewSet)