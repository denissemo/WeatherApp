from django.urls import path
from . import views
from .views import SimpleWeatherView


urlpatterns = [
    path('', views.index, name="index"),
    path('current-city/', SimpleWeatherView.as_view(), name='current-city')
]
