from django.shortcuts import render

from .forms import DemoForm

# Create your views here.

def index(request):
    form = DemoForm()
    return render(request, "index.html", {"form": form})
