from django.contrib import admin

from paciente.models import Paciente

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    pass
