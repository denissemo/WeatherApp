from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class LogInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username foes not exist")
        user = User.objects.get(username=username)
        if not user.check_password(password):
            raise forms.ValidationError("Incorrect password")


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "first_name",
            "last_name",
            "email"
        ]

    def clean(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("User already exist")
