from django.db import models

# Create your models here.

class Car(models.Model):
    model=models.CharField(max_length=512)
    color=models.CharField(max_length=250)
    price=models.DecimalField(max_digits=10,decimal_places=3)
    invented_year=models.DateField()
