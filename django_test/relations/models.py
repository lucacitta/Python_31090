from django.db import models

class Car_owner(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

class Colors(models.Model):
    name = models.CharField(max_length=50)


class Car(models.Model):
    owner = models.OneToOneField(Car_owner, on_delete=models.CASCADE, related_name='owned_car')
    color = models.ForeignKey(Colors, on_delete=models.SET_NULL, null=True, blank=True, related_name='car')

class Car_driver(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    cars = models.ManyToManyField(Car, related_name='drivers')
