from .models import MarketingMessage

class DisplayMarketing():
	def process_request(self, request):
		try:
			request.session['marketing_message'] = MarketingMessage.objects.get_featured_item().message
		except:
			request.session['marketing_message'] = False