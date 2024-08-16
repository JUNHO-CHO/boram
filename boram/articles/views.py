from django.shortcuts import render

# Create your views here.
def index(request):
	response = HttpResponse("<h1>Hello, Django!</h1>") 
	return response