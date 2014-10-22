import stripe

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import post_save




from .models import UserStripe

stripe.api_key = settings.STRIPE_SECRET_KEY

User = get_user_model()


# if we decide to change how we want to add the stripe id, this is where we set it for a user_logged_in
# def get_or_create_stripe(sender, user, *args, **kwargs):
# 	try:
# 		user.userstripe.stripe_id
# 	except UserStripe.DoesNotExist:
# 		customer = stripe.Customer.create(
#   			email = str(user.email)
# 		)
# 		new_user_stripe = UserStripe.objects.create(
# 			 	user=user,
# 			 	stripe_id = customer.id
# 			 	)
# 	except:
# 		pass
# # user_logged_in.connect(get_or_create_stripe)

def get_create_stripe(user):
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

def user_created(sender, instance, created, *args, **kwargs):
	user = instance
	if created:
		get_create_stripe(user)
		#send our email



post_save.connect(user_created, sender=User)















