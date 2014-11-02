from django.contrib import admin

# Register your models here.
from .models import UserStripe, EmailConfirmed, EmailMarketingSignUp


admin.site.register(UserStripe)

admin.site.register(EmailConfirmed)


class EmailMarketingSignUpAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'timestamp']
	class Meta:
		model = EmailMarketingSignUp


admin.site.register(EmailMarketingSignUp, EmailMarketingSignUpAdmin)