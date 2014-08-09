import time

from django.core.urlresolvers import reverse
from django.shortcuts import render, HttpResponseRedirect

# Create your views here.

from carts.models import Cart

from .models import Order


def checkout(request):

	try:
		the_id = request.session['cart_id']
		cart = Cart.objects.get(id=the_id)
	except:
		the_id = None
		#return HttpResponseRedirect("/cart/")
		return HttpResponseRedirect(reverse("cart"))
		
	new_order, created = Order.objects.get_or_create(cart=cart)
	if created:
		new_order.order_id = str(time.time())
		new_order.save()

	if new_order.status == "Finished":
		del request.session['cart_id']
		del request.session['items_total']
		return HttpResponseRedirect(reverse("cart"))

	context = {}
	template = "products/home.html"
	return render(request, template, context)