from django.shortcuts import render

# Create your views here.

def abc(request):

	template = 'home.html'
	context = locals()
	return render(request, template, context)