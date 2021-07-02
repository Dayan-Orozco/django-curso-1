from django.contrib import admin
from .models import Persona
# importo el modelo de persona para añadir el modelo en el sitio de administracion
admin.site.register(Persona)