# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from .models import Sensor, Measurement
from .serializers import MeasurementSerializer, SensorDetailSerializer, SensorsSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView


class SensorsView(ListCreateAPIView):
    """Просмотр списка датчиков с названием (name) и описанием (description) c возможностью изменения"""
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerializer


class SensorView(RetrieveUpdateAPIView):
    """Датчик с названием и описанием с возможностью изменения"""
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementView(RetrieveUpdateAPIView):
    """Измерения с возможностью добавления измерений"""
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
