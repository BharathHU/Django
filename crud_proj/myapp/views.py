from django.shortcuts import render
from django.views.generic import *
from .models import *
from django.urls import reverse_lazy
# Create your views here.

class Studentlist(ListView):
    model=Student
    # defalt context-> student_list
    # defalttemplates -> student_list.html

class StudentDetails(DetailView):
    model=Student
    # defalt context-> student
    # defalttemplates -> student_details.html
    

class StudentUpdate(UpdateView):
    model=Student
    fields='__all__'

class StudentDelete(DeleteView):
    model=Student
    success_url=reverse_lazy('student')
    #default context :student
    #default templates :student_details.html
    