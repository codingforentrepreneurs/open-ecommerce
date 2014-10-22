import re

from django.shortcuts import render, HttpResponseRedirect, Http404
from django.contrib.auth import logout, login, authenticate

from .forms import LoginForm, RegistrationForm
from .models import EmailConfirmed
# Create your views here.

def logout_view(request):
	print "logging out"
	logout(request)
	return HttpResponseRedirect('/')

def login_view(request):
	form = LoginForm(request.POST or None)
	btn = "Login"
	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(username=username, password=password)
		login(request, user)

	context = {
		"form": form,
		"submit_btn": btn,
	}
	return render(request, "form.html", context)


def registration_view(request):
	form = RegistrationForm(request.POST or None)
	btn = "Join"
	if form.is_valid():
		new_user = form.save(commit=False)
		# new_user.first_name = "Justin" this is where you can do stuff with the model form
		new_user.save()
		# username = form.cleaned_data['username']
		# password = form.cleaned_data['password']
		# user = authenticate(username=username, password=password)
		# login(request, user)

	context = {
		 "form": form,
		 "submit_btn": btn,
	}
	return render(request, "form.html", context)


SHA1_RE = re.compile('^[a-f0-9]{40}$')

def activation_view(request, activation_key):
	if SHA1_RE.search(activation_key):
		print "activation key is real"
		try:
			instance = EmailConfirmed.objects.get(activation_key=activation_key)
		except EmailConfirmed.DoesNotExist:
			instance = None
			raise Http404
		if instance is not None and not instance.confirmed:
			page_message = "Confirmation Successful! Welcome."
			instance.confirmed = True
			instance.activation_key = "Confirmed"
			instance.save()
		elif instance is not None and instance.confirmed:
			page_message = "Already Confirmed"
		else:
			page_message = ""

		context = {"page_message": page_message}
		return render(request, "accounts/activation_complete.html", context)
	else:
		raise Http404
























