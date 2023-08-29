from django.db import models

# Create your models here.



class Machine(models.Model):
    name               = models.CharField(max_length=50 ,default="")
    numbers             = models.CharField(max_length=50 ,default="")
    characteristics    = models.CharField(max_length=50 ,default="")
    materials             = models.CharField(max_length=50 ,default="")
    moter            = models.CharField(max_length=50 ,default="") 
    
    def __str__(self):
        return self.name
