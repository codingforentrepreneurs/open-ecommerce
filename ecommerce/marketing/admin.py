from django.contrib import admin

# Register your models here.
from .models import MarketingMessage


class MarketingMessageAdmin(admin.ModelAdmin):
	class Meta:
		model = MarketingMessage

admin.site.register(MarketingMessage, MarketingMessageAdmin)