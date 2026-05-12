from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    email=models.EmailField()
    place=models.CharField(max_length=100)
    dob=models.DateField()

    def __str__(self):
        return self.name