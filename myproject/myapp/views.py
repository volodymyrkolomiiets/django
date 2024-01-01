from django.shortcuts import render
from myapp.forms import LogForm

# Create your views here.

def form_views(request):
    form = LogForm()
    if request.method == "POST":
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
        
    context = {"form": form}
    return render(request, "index.html", context)
