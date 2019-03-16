from django.shortcuts import render
from .weather_models import SimpleWeather
from django.views import View


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
