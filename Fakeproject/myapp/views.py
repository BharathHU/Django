from django.shortcuts import render
from .models import Employee

# Create your views here.
def myview(request):
    employees = Employee.objects.all()
    return render(request,'fake.html',{'employees':employees})

