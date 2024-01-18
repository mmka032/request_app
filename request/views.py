from django.shortcuts import render
from django.http import HttpResponse

from .weatherari import fetch_weather

def index(request):
    return render(request, 'request/index.html')

def detail(request):
    print("----------------------------------------------")
    place = request.POST["place"]
        
    weather_deta = fetch_weather(place)
    context = {
        "weather_deta": weather_deta,
    }


    return render(request, 'request/detail.html', context)