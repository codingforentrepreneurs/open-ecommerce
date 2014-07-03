from django.db import models
# Create your models here.

class Product(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(null=True, blank=True)
	price = models.DecimalField(decimal_places=2, max_digits=100, default=29.99)
	sale_price = models.DecimalField(decimal_places=2, max_digits=100,\
												null=True, blank=True)
	#image = models.FileField(upload_to='products/images/', null=True)
	slug = models.SlugField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return "this is a product"

	def get_price(self):
		return self.price

### FOR IMAGE FIELD ## INSTALL PILLOW

#ARCHFLAGS=-Wno-error=unused-command-line-argument-hard-error-in-future pip install pillow

#export CFLAGS=-Qunused-arguments
#export CPPFLAGS=-Qunused-arguments
#pip install pillow

#use homebrew: #install with: 
#ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"

#in terminal:
#brew tap Homebrew/python
#brew install pillow



