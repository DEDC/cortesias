from django.contrib import admin
from .models import Eventos, Localidades, Solicitante, Solicitud

admin.site.register(Eventos)
admin.site.register(Localidades)
admin.site.register(Solicitante)
admin.site.register(Solicitud)

