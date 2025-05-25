from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def committee_page(request, committee=None):
    return None

def involvement(request):
    return render(request, 'home/involvement.html')

def beday(request):
    return None

def lexpo(request):
    return None

def mid(request):
    return None
