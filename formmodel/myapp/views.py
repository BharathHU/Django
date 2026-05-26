from django.shortcuts import render
from myapp.forms import StudentForm
from django.http import HttpResponse
# Create your views here.
def formview(request):
    f=StudentForm()
    if request.method=='POST':
        f=StudentForm(request.POST)
        if f.is_valid():
            f.save()
    return render(request, 'form.html', {'form': f})