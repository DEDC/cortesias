from django.urls import path
from .views import vCortesias, vObtenerEvento

app_name = 'solicitud'

urlpatterns = [
    path('', vCortesias, name = 'principal'),
    #--- AJAX
    path('ajax/event/<int:id>', vObtenerEvento, name = 'obEvento'),
]