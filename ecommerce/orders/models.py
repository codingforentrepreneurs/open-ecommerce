from django.db import models

# Create your models here.
from carts.models import Cart

STATUS_CHOICES = (
		("Started", "Started"),
		("Abandoned", "Abandoned"),
		("Finished", "Finished"),
	)

#python tuples

class Order(models.Model):
	#add user
	# address **
	order_id = models.CharField(max_length=120, default='ABC', unique=True)
	cart = models.ForeignKey(Cart)
	status = models.CharField(max_length=120, choices=STATUS_CHOICES, default="Started")
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.order_id