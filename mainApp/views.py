from django.shortcuts import render
from django.contrib.auth import get_user_model, authenticate, login
from django.http import HttpResponseRedirect
from django.views import View

from .weather_models import SimpleWeather
from .forms import SignUpForm, LogInForm
from .models import UserAccount


def index(request):
    return render(request, 'mainPage/index.html')


class SimpleWeatherView(View):
    template = 'current-city/current-city.html'

    def get(self, *args, **kwargs):
        simpleWeather = SimpleWeather(self.request.GET['city'])
        # this use for jinja
        context = {
            'cities': simpleWeather
        }
        return render(self.request, self.template, context)
