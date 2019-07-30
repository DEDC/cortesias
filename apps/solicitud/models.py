from django.db import models

class Eventos(models.Model):
    nombre = models.CharField(max_length =  100)
    fecha = models.DateTimeField()
    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
    
    def __str__(self):
        return self.nombre 

class Localidades(models.Model):
    nombre = models.CharField(max_length =  100)
    shortname = models.CharField(max_length =  100)
    class Meta:
        verbose_name = "Localidad"
        verbose_name_plural = "Localidades"
    
    def __str__(self):
        return self.nombre

class Solicitante(models.Model):
    nombre = models.CharField(max_length =  100)
    class Meta:
        verbose_name = "Solicitante"
        verbose_name_plural = "Solicitantes"
    def __str__(self):
        return self.nombre

class Solicitud(models.Model):
    evento = models.ForeignKey(Eventos, related_name = 'solicitud', on_delete = models.CASCADE)
    localidad = models.ForeignKey(Localidades, related_name = 'localidad', on_delete = models.PROTECT)
    solicitante = models.ForeignKey(Solicitante, related_name = 'solicitante', on_delete = models.PROTECT)
    cantidad = models.IntegerField()
    extra = models.CharField(max_length = 200, null = True, blank = True)
    class Meta:
        verbose_name = "Solicitud"
        verbose_name_plural = "Solicitudes"