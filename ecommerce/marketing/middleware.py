from .models import MarketingMessage

class DisplayMarketing():
	def process_request(self, request):
		try:
			request.session['marketing_message'] = MarketingMessage.objects.all()[0].message
		except:
			request.session['marketing_message'] = False