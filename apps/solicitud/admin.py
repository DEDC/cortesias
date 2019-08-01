from django.contrib import admin
from .models import Eventos, Localidades, Solicitante, Solicitud

class SolicitudesAdmin(admin.ModelAdmin):
    list_display = ('cantidad','evento', 'localidad', 'solicitante', 'extra')
    list_display_links = ('evento',)
    list_filter = ('evento',)
    ordering = ['evento']

admin.site.register(Eventos)
admin.site.register(Localidades)
admin.site.register(Solicitante)
admin.site.register(Solicitud, SolicitudesAdmin)

