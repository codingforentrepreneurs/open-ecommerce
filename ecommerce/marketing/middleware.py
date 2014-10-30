import datetime

from django.utils import timezone

from .models import MarketingMessage

def is_offset_greater(time_string_offset):
	 time1 = str(timezone.now())[:19]
	 offset_time = time_string_offset[:19] #to remove extra, unnecessary numbers
	 offset_time_formated = datetime.datetime.strptime(offset_time, "%Y-%m-%d %H:%M:%S" )
	 offset_time_tz_aware = timezone.make_aware(offset_time_formated, timezone.get_default_timezone())
	 now_time_formated = datetime.datetime.strptime(time1, "%Y-%m-%d %H:%M:%S" )
	 now_time_tz_aware = timezone.make_aware(now_time_formated, timezone.get_default_timezone())
	 return now_time_tz_aware > offset_time_tz_aware



class DisplayMarketing():
	def process_request(self, request):
		try:
			message_offset = request.session['dismiss_message_for'] #as string
		except:
			message_offset = None

		try:
			marketing_message = MarketingMessage.objects.get_featured_item().message
		except:
			marketing_message = False

		if message_offset is None:
			request.session['marketing_message'] = marketing_message
		elif message_offset is not None and is_offset_greater(message_offset):
			request.session['marketing_message'] = marketing_message
		else:
			try:
				del request.session['marketing_message'] 
			except:
				pass