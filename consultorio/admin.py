from django.contrib import admin
from consultorio.models import Consultorio

@admin.register(Consultorio)
class ConsultorioAdmin(admin.ModelAdmin):
    pass

