from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Sum
from django.utils.dateformat import format
from .models import Eventos, Solicitud

def vCortesias(request):
    eventos = Eventos.objects.all()
    context = {'eventos' : eventos}
    return render(request, 'site/cortesias.html', context)

def vObtenerEvento(request, id):
    if request.is_ajax():
        if id == 0:
            total_by_localities = list(Solicitud.objects.values('localidad__nombre').annotate(Sum('cantidad')))
            total = Solicitud.objects.aggregate(total = Sum('cantidad'))
            data = {
                'status' : 'success',
                'event' : 'Todos los partidos',
                'datetime' : 'Todas las fechas',
                'total_by_localities' : total_by_localities,
                'total' : total.get('total')
            }
        elif id > 0:
            evento = get_object_or_404(Eventos, pk = id)
            total_by_localities = list(evento.solicitud.values('localidad__nombre').annotate(Sum('cantidad')))
            total = evento.solicitud.aggregate(total = Sum('cantidad'))
            data = {
                'status' : 'success',
                'event' : evento.nombre,
                'datetime' : format(evento.fecha, 'l d \d\e F \d\e Y'),
                'total_by_localities' : total_by_localities,
                'total' : total.get('total')
            }
        return JsonResponse(data, safe = False)