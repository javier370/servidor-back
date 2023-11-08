from django.urls import path
from rest_framework.routers import DefaultRouter
from cita.api.views import CitaApiViewSet

router_citas = DefaultRouter()
router_citas.register(prefix='citas', basename='citas', viewset=CitaApiViewSet)