from django.shortcuts import render
from .oauth import data

def home_page(request):
    return render(request, 'home.html', {'data': data})
