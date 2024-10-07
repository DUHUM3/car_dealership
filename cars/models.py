from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='car_images/', blank=True, null=True) 
    def __str__(self):
        return f"{self.name} ({self.year})"
