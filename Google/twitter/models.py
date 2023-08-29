from django.db import models

# Create your models here.



class school(models.Model):
    name                = models.CharField(max_length=50 ,default="")
    father_name         = models.CharField(max_length=50 ,default="")
    gender              = models.CharField(max_length=50 ,default="")
    Class               = models.CharField(max_length=50 ,default="")
    section             = models.CharField(max_length=50 ,default="") 
    roll_no             = models.CharField(max_length=50 ,default="")
    def __str__(self):
        return self.name


