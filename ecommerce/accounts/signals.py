import stripe

from django.conf import settings
from django.contrib.auth.signals import user_logged_in


from .models import UserStripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def get_or_create_stripe(sender, user, *args, **kwargs):
	try:
		user.userstripe.stripe_id
	except UserStripe.DoesNotExist:
		customer = stripe.Customer.create(
  			email = str(user.email)
		)
		new_user_stripe = UserStripe.objects.create(
			 	user=user,
			 	stripe_id = customer.id
			 	)
	except:
		pass


user_logged_in.connect(get_or_create_stripe)