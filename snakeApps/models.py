from django.db import models

# Create your models here.

class Snake(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=500)
    color_or_pattern=models.CharField(max_length=100)
    favourite_prey=models.CharField(max_length=100)
    region=models.CharField(max_length=50)
    venomous=models.CharField(max_length=4)
    imagePath=models.CharField(max_length=200)