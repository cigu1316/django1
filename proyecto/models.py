from django.db import models

class Products(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    stock = models.BooleanField()
   
   