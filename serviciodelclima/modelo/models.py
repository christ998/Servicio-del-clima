from django.db import models

# Create your models here.

class Ciudades(models.Model):
    ciudad = models.CharField(max_length=30)
    id = models.IntegerField(primary_key=True)