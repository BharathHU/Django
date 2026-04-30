from django.shortcuts import render
from django.http import HttpResponse
def view2(request):
    a="<h1><i>this is the response from Second app"
    return HttpResponse(a)

# Create your views here.
