from django.db import models

# Create your models here.


class house(models.Model):
    city             = models.CharField(max_length=50 ,default="")
    mohallah_no         = models.CharField(max_length=50 ,default="")
    street_no              = models.CharField(max_length=50 ,default="")
    house_no               = models.CharField(max_length=50 ,default="")
    rooms             = models.CharField(max_length=50 ,default="") 
                 
    def __str__(self):
        return self.city