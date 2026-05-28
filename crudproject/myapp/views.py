from django.shortcuts import render
from myapp.models import Employee

# Create your views here.
def display(request):
    e=Employee.objects.all()
    d={'emp':e}
    return render(request,'display.html',d)
