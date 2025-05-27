from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Committee

def index(request):
    return render(request, 'home/index.html')

def committee_page(request, committee=None):
    comtext = get_object_or_404(Committee, pk=committee)  # committee context
    officers = comtext.get_officers()
    return render(request, 'home/committee.html', {"committee": comtext, "officers": officers})

def involvement(request):
    return render(request, 'home/involvement.html')

def beday(request):
    return render(request, 'home/beday.html')

def lexpo(request):
    return render(request, 'home/lexpo.html')

def mid(request):
    return render(request, 'home/mid.html')
