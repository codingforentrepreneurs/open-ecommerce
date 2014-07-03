from django.shortcuts import render

# Create your views here.

from .models import Product

def home(request):
	if request.user.is_authenticated():
		username_is = "Justin using context"
		context = {"username_is": request.user}
	else:
		context = {"username_is": request.user}
	
	template = 'products/home.html'	
	return render(request, template, context)


def all(request):
	products = Product.objects.all()
	context = {'products': products}
	template = 'products/all.html'	
	return render(request, template, context)