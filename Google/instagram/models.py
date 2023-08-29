from django.db import models

# Create your models here.


class CNIC(models.Model):
    name               = models.CharField(max_length=50 ,default="")
    father_name             = models.CharField(max_length=50 ,default="")
    gender    = models.CharField(max_length=50 ,default="")
    country            = models.CharField(max_length=50 ,default="")
    date_birth            = models.CharField(max_length=50 ,default="") 
    
    def __str__(self):
        return self.name
