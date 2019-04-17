from django.shortcuts import render
from django.views import View
from .weather_models import Weather
from .models import City, Day
from django.http import HttpResponse
import calendar
import datetime


def index(request):
    return render(request, 'mainPage/index.html')


def cities(request):
    template = 'city/cities_template.html'
    city = City.objects.in_bulk()  # return data in dict format example: {1: <City: Vinnytsia>, 2: <City: Kyiv>}
    day = Day.objects.in_bulk()
    days = list(set([day[id_].date for id_ in day]))
    days.sort()
    context = {
        'cities': [city[id_].name for id_ in city],
        'days': days
    }
    return render(request, template, context)
