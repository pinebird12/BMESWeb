from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'home/index.html')

def committee_page(request, committee=None):
    return None

def involvement(request):
    return render(request, 'home/involvement.html')

def beday(request):
    return render(request, 'home/beday.html')

def lexpo(request):
    return render(request, 'home/lexpo.html')

def mid(request):
    return render(request, 'home/mid.html')
