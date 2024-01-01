from django.shortcuts import render
from .forms import ApplicationForm, InputForm

# Create your views here.

def index(request):
    form = ApplicationForm()
    return render(request, "index.html", {"form":form})

def form_views(request):
    form = InputForm()
    context = {"form":form}
    return render(request, "index.html", context)