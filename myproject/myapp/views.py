from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home1(request):
    return HttpResponse("Welcome to Littlr lrmon restorant!")


def home(request):
    return render(request, "home.html", {})

def register(request):
    return render(request, "register.html", {})

def login(request):
    return render(request, "login.html", {})