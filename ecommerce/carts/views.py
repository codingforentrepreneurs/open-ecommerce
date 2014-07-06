from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.

from products.models import Product

from .models import Cart

def view(request):
	try:
		the_id = request.session['cart_id']
	except:
		the_id = None
	if the_id:
		cart = Cart.objects.get(id=the_id)
		context = {"cart": cart}
	else:
		empty_message = "Your Cart is Empty, please keep shopping."
		context = {"empty": True, "empty_message": empty_message}
	
	template = "cart/view.html"
	return render(request, template, context)


def update_cart(request, slug):
	request.session.set_expiry(120000)
	try:
		the_id = request.session['cart_id']
	except:
		new_cart = Cart()
		new_cart.save()
		request.session['cart_id'] = new_cart.id
		the_id = new_cart.id
	
	cart = Cart.objects.get(id=the_id)

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

	request.session['items_total'] = cart.products.count()
	cart.total = new_total
	cart.save()

	return HttpResponseRedirect(reverse("cart"))