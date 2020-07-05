from django.http import HttpResponse
from django.shortcuts import render

def terms(request):
    return render(request, 'terms.html')

def privacy(request):
    return render(request, 'privacy.html')
