from django.db import models

# Create your models here.
class Breed(models.Model):
    name = models.CharField(max_length=22)
    color = models.CharField(max_length=22)
    size = models.PositiveIntegerField()
    friendliness = models.CharField(max_length=22)

