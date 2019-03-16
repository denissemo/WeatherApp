from django.urls import path, reverse_lazy
from django.contrib.auth.views import LogoutView
from . import views
from .views import SimpleWeatherView, SignUpView, LogInView


urlpatterns = [
    path('', views.index, name="index"),
    path('current-city/', SimpleWeatherView.as_view(), name='current-city'),
    path('sign_up/', SignUpView.as_view(), name="sign_up"),
    path('log_in/', LogInView.as_view(), name="log_in"),
    # path('user_account/<user>/', UserAccountView.as_view(),
    #      name="account_view"),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy("index")),
         name="logout")
]
