from django.shortcuts import redirect, render
from myapp.forms import EmployeeForm
from myapp.models import Employee

# Create your views here.
def display(request):
    e=Employee.objects.all()
    d={'emp':e}
    return render(request,'display.html',d)

def insert_view(request):
    f=EmployeeForm()
    if request.method=='POST':
        f=EmployeeForm(request.POST)
        if f.is_valid():
            f.save(commit=True)
            return redirect ('/')
    d={'form':f}
    return render(request,'insert.html',d)
    
