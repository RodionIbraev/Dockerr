from django.db import models


class Sensor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class Measurement(models.Model):
    sensor = models.ForeignKey(
        'Sensor',
        on_delete=models.CASCADE
    )
    temperature = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
