from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from account.models import Profile

# Create your views here.

def home(request):
    return render(request, "home.html")


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        role = request.POST.get("role")

        if not username or not password or not role:
            # Simple fallback; you can add proper error messages later.
            return render(request, "register.html")

        # Avoid duplicate usernames (would otherwise error on Profile/User creation)
        if User.objects.filter(username=username).exists():
            return render(request, "register.html")

        user = User.objects.create(
            username=username,
            password=make_password(password),
        )
        Profile.objects.create(user=user, role=role)

        return redirect("home")

    return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")

        # Invalid credentials
        return render(request, "login.html", {"error": "Invalid username or password"})

    return render(request, "login.html")


