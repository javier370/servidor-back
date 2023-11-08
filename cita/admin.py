from django.contrib import admin
from cita.models import Cita

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    pass
