from django.db import models

# Create your models here.

class Ciudades(models.Model):
    ciudad = models.CharField(max_length=30, null=False)
    ident=models.IntegerField()
