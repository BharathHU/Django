from django.shortcuts import render
from django.http import HttpResponse
def view1(request):
    a="this is the response from first app"
    return HttpResponse(a)

# Create your views here.
