from django.shortcuts import render, Http404

# Create your views here.

from .models import Product

def home(request):
	products = Product.objects.all()
	template = 'products/home.html'	
	context = {"products": products}
	return render(request, template, context)


def all(request):
	products = Product.objects.all()
	context = {'products': products}
	template = 'products/all.html'	
	return render(request, template, context)


