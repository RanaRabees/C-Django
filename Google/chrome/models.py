from unicodedata import name
from django.db import models

# Create your models here.

class animal(models.Model):
    name         = models.CharField(max_length=50 ,default="")
    age          = models.CharField(max_length=50 ,default="")
    height       = models.CharField(max_length=50 ,default="")
    weight       = models.CharField(max_length=50 ,default="")
    colour       = models.CharField(max_length=50 ,default="") 
    type         = models.CharField(max_length=50 ,default="")
    def __str__(self):
        return self.name



