from django.shortcuts import render
from .models import Employee

# Create your views here.

def home_view(request):
    return render(request, 'ormApp/home.html')