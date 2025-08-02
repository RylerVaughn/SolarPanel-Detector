from django.db import models

# Create your models here.
class Client(models.Model):
    address = models.CharField(max_length=1000)
    last_accessed = models.DateField()
    notes = models.TextField(blank=True)
    longitude = models.FloatField(default=0)
    latitude = models.FloatField(default=0)
    color = models.IntegerField(default=0)
    name = models.CharField(max_length=100, default="Null")
    phone_number = models.CharField(max_length=15, default='')
    
    def __str__(self):
        return self.name

class Job(models.Model):
    payment = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE, related_name="jobs")
    date = models.DateField()

    def __str__(self):
        return f"Job done for: {self.client}, completed {self.date}"