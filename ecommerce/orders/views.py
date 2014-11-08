import time

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, HttpResponseRedirect

# Create your views here.

from accounts.forms import UserAddressForm
from accounts.models import UserAddress
from carts.models import Cart

from .models import Order
from .utils import id_generator

def orders(request):
	context = {}
	template = "orders/user.html"
	return render(request, template, context)


#require user login ** 
@login_required
def checkout(request):
	try:
		the_id = request.session['cart_id']
		cart = Cart.objects.get(id=the_id)
	except:
		the_id = None
		#return HttpResponseRedirect("/cart/")
		return HttpResponseRedirect(reverse("cart"))
	
	try:
		new_order = Order.objects.get(cart=cart)
	except Order.DoesNotExist:
		new_order = Order()
		new_order.cart = cart
		new_order.user = request.user
		new_order.order_id = id_generator()
		new_order.save()
	except:
		# work on some error message
		return HttpResponseRedirect(reverse("cart"))

	try:
		address_added = request.GET.get("address_added")
	except:
		address_added = None

	if address_added is None:
		address_form = UserAddressForm()
	else:
		address_form = None

	current_addresses = UserAddress.objects.filter(user=request.user)
	billing_addresses = UserAddress.objects.get_billing_addresses(user=request.user)
	print billing_addresses
	##1 add shipping address
	##2 add billing address
	#3 add and run credit card 
	if new_order.status == "Finished":
		#cart.delete()
		del request.session['cart_id']
		del request.session['items_total']
		return HttpResponseRedirect(reverse("cart"))

	context = {
	"address_form": address_form,
	"current_addresses": current_addresses,
	"billing_addresses": billing_addresses,
	}
	template = "orders/checkout.html"
	return render(request, template, context)




