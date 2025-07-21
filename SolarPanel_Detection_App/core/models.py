from django.db import models

# Create your models here.
class Marker(models.Model):
    address = models.CharField(max_length=1000)
    last_accessed = models.DateField()
    notes = models.TextField(blank=True)
    longitude = models.FloatField(default=0)
    latitude = models.FloatField(default=0)
    color = models.IntegerField(default=0)

    def __str__(self):
        return self.address
