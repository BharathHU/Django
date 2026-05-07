from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view(request):
    s="Welcome to Django sessionn!!"
    return HttpResponse(s)