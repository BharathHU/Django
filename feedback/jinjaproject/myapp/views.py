from django.shortcuts import render

# Create your views here.
def demo(request):
    n1="Bharath"
    n2="Vishal"
    p1="Adhishakti Hotel"
    ctx={'name1':n1,'name2':n2,'place':p1}
    return render(request,'myapp/demo.html',ctx)
