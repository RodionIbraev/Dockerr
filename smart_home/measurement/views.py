from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response

from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, MeasurementSerializer, MeasurementSerializerFilter


# изменение датчика / получение информации по датчику
class RetrieveUpdateSensor(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def get(self, request, pk):
        measurements = Measurement.objects.filter(sensor=pk)
        response = SensorDetailSerializer(RetrieveAPIView.get(self, request).data).data
        response['measurements'] = MeasurementSerializerFilter(measurements, many=True).data
        return Response(response)


# добавление измерения
class CreateMeasurement(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


# получение списка датчиков / создание датчика
class ListCreateSensors(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


