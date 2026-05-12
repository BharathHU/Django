from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    place = models.CharField(max_length=100)
    email= models.EmailField()
    job= models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)