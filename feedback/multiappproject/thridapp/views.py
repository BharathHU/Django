from django.shortcuts import render
from django.http import HttpResponse
def view3(request):
    a="<h1><i>this is the response from Third app"
    return HttpResponse(a)

# Create your views here.
