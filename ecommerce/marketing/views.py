import json
import datetime

from django.conf import settings
from django.shortcuts import render, HttpResponse, Http404
from django.utils import timezone

from .forms import EmailForm
# Create your views here.

def dismiss_marketing_message(request):
	if request.is_ajax():
		data = {"success": True}
		print data
		json_data = json.dumps(data)
		request.session['dismiss_message_for'] = str(timezone.now() +\
					 datetime.timedelta(hours=settings.MARKETING_HOURS_OFFSET,\
					  seconds=settings.MARKETING_SECONDS_OFFSET))
		print json_data
		return HttpResponse(json_data, content_type='application/json')
	else:
		raise Http404


def email_signup(request):
	if request.method == "POST":
		form = EmailForm(request.POST)
		if form.is_valid():
			email= form.cleaned_data['email']
			return HttpResponse('Success %s' %(email))
		if form.errors:
			print form.errors
			json_data = json.dumps(form.errors)
			return HttpResponse(json_data, content_type='application/json')
	else:
		raise Http404
