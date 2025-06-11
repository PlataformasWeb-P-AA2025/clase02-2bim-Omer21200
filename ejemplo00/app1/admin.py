from django.contrib import admin

# Register your models here.
# Importar las clases del modelo
from app1.models import Estudiante
from app1.models import Ciudad

admin.site.register(Estudiante)
admin.site.register(Ciudad)
