from django.contrib import admin

# Register your models here.
from persona.models import Persona, Domiciolio

admin.site.register(Persona)
admin.site.register(Domiciolio)