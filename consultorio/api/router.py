from django.urls import path
from rest_framework.routers import DefaultRouter

from consultorio.api.views import ConsultorioApiViewSet

router_consultorios = DefaultRouter()
router_consultorios.register(prefix='consultorios', basename='consultorios', viewset=ConsultorioApiViewSet)