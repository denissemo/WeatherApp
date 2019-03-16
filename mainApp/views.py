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


User = get_user_model()


class SignUpView(View):
    template = "mainPage/sign_up.html"

    def get(self, request, *args, **kwargs):
        form = SignUpForm(request.POST or None)
        context = {
            "form": form
        }
        return render(self.request, self.template, context)

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            new_user.set_password(password)
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            new_user.save()
            UserAccount.objects.create(
                user=User.objects.get(username=new_user.username),
                first_name=new_user.first_name,
                email=new_user.email)
            return HttpResponseRedirect("/")
        context = {
            "form": form
        }
        return render(self.request, self.template, context)


class LogInView(View):
    template = "mainPage/login.html"

    def get(self, request, *args, **kwargs):
        form = LogInForm()
        context = {
            "form": form
        }
        return render(self.request, self.template, context)

    def post(self, request, *args, **kwargs):
        form = LogInForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(self.request, user)
                return HttpResponseRedirect("/")
        context = {
            "form": form
        }
        return render(self.request, self.template, context)

# change !!!
# class UserAccountView(View):
#     template = "user_account.html"
#
#     def get(self, *args, **kwargs):
#         user = self.kwargs.get("user")
#         current_user = UserAccount.objects.get(user=User.objects.get(username=user))
#         context = {
#             "current_user": current_user
#         }
#         return render(self.request, self.template, context)
