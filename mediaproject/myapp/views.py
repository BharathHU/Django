from django.shortcuts import render
from .models import Product

# Create your views here.
def productview(request):
    products = Product.objects.all()
    d = {'products': products}
    return render(request, 'product.html', d)

