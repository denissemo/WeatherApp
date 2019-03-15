from django.shortcuts import render
from .weather_models import SimpleWeather


def index(request):
    print(request.GET['city'])
    SimpleWeather(request.GET['city'])
    return render(request, 'mainPage/index.html')
