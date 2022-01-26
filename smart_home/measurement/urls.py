from django.urls import path
from .views import ListCreateSensors, RetrieveUpdateSensor, CreateMeasurement

urlpatterns = [
    path('sensors/', ListCreateSensors.as_view()),
    path('sensors/<pk>/', RetrieveUpdateSensor.as_view()),
    path('measurements/', CreateMeasurement.as_view()),
]
