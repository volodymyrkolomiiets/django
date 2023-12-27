from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.urls import reverse
# Create your views here.


def index(request):
    return HttpResponse("<h1> Hello world! From demoapp!!! </h1>")


def login(request):
    return HttpResponse("This endpoint have to implement loging system ")


def myview(request):
    return HttpResponsePermanentRedirect(reverse('newapp:index'))
