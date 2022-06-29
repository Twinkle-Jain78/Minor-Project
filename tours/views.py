from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def Register(request):
    return render(request, "Register.html")


