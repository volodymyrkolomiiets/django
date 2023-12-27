from django.http import HttpResponse, HttpResponseNotFound

def handler404(request, exception):
    return HttpResponse("<h1> 404: Page not Found!<h1> <br> <br> <button onclick="" href='';"">Go to Home page</button>" )

def home(request):
    # return HttpResponse(" Hello from Home !")
    return HttpResponseNotFound(" Hello from Home !")
    