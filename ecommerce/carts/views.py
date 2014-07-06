from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.

from products.models import Product

from .models import Cart

def view(request):
	cart = Cart.objects.all()[0]
	context = {"cart": cart}
	template = "cart/view.html"
	return render(request, template, context)


def update_cart(request, slug):
	cart = Cart.objects.all()[0]
	try:
		product = Product.objects.get(slug=slug)
	except Product.DoesNotExist:
		pass
	except:
		pass
	if not product in cart.products.all():
		cart.products.add(product)
	else:
		cart.products.remove(product)

	new_total = 0.00
	for item in cart.products.all():
		new_total += float(item.price)

	cart.total = new_total
	cart.save()

	return HttpResponseRedirect(reverse("cart"))