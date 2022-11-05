from django.db import models
#from datetime import datetime


# Create your models here.
class bd_familiares(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
  #  fecha = models.datef()

