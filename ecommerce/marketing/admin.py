from django.contrib import admin

# Register your models here.
from .models import MarketingMessage


class MarketingMessageAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "start_date", "end_date", "active", "featured"]
	class Meta:
		model = MarketingMessage

admin.site.register(MarketingMessage, MarketingMessageAdmin)