from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required 
from django.contrib.auth.mixins import PermissionRequiredMixin 
from django.views.generic import ListView 
from .models import Product


def my_view(request):
    if request.user.is_anonymous:
        raise PermissionDenied()
    return HttpResponse("<h1>Hello</h1>")


@login_required
def index(request):
    return HttpResponse("Hello world")


def testpermission(user):
    if user.is_authenticated and user.has_perm("myapp.change_category"):
        return True
    else:
        return False
    

@user_passes_test(testpermission)
def change_ctg(request):
    return HttpResponse("Hello")




@permission_required("myapp.change_category") 
def store_creator(request): 
    # Logic for making change to category of product model instance    
    pass

class ProductListView(PermissionRequiredMixin, ListView): 
    permission_required = "myapp.view_product" 
    template_name = "product.html" 
    model = Product