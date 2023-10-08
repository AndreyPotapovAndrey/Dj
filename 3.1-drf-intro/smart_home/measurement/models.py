from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'


class Measurement(models.Model):
    measure = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurement', verbose_name='Датчик')
    temperature = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Температура')
    change = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.change)

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'
