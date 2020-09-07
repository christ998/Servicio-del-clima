from django.db import models

# Create your models here.

class Ciudades(models.Model):
    ciudad = models.CharField(max_length=30, null=False, unique=True)
    ident=models.IntegerField()

    def __str__(self):
        return self.ciudad
