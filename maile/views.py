from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from .forms import RegistrationForm
from .models import User
# Create your views here.

@login_required(login_url='/login')
def index(request):
    return render(request, "maile/index.html")


def login_view(request):
    if request.method == "POST":

        email = request.POST["email"]
        password = request.POST["password"]

        # Attempt to sign user in
        user = authenticate(request, email=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "maile/login.html", {
                "message": "Invalid username and/or password.",
                "userForm": RegistrationForm()
            })
    else:
        return render(request, "maile/login.html", {
            "userForm": RegistrationForm()
        })


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid() == True:
            first_name = form.cleaned_data["firstName"]
            last_name = form.cleaned_data["lastName"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            # Ensure password matches confirmation
            confirmation = request.POST["confirmPassword"]
            if password != confirmation:
                return render(request, "maile/register.html", {
                    "message": "Passwords must match.",
                    "userForm": RegistrationForm()
                })
            user = User.objects.create_user(first_name, last_name, email, password)
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "maile/register.html", {
                "message": "email already exists.",
                "userForm": RegistrationForm()
            })
    else:
        return render(request, "maile/register.html", {
            "userForm": RegistrationForm()
        })
