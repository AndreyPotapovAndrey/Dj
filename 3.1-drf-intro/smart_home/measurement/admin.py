from django.contrib import admin

from django.contrib import admin
from .models import Sensor, Measurement


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


@admin.register(Measurement)
class MeasurementsAdmin(admin.ModelAdmin):
    list_display = ['measure', 'temperature', 'change']
