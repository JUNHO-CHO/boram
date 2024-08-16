from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
	response = HttpResponse("<h1>Hello, Django!</h1>") 
	return response