from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import (login_required,
                                            user_passes_test,
                                            permission_required)
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView

from .models import Product

# Create your views here.

def my_view(request):
    if request.user.is_anonymous:
        raise PermissionDenied()


@login_required
def index(request):
    return HttpResponse("Hello from index!")

def testpermission(user):
    if user.is_authenticated and user.has_perm("myapp.can_change_category"):
        return True
    else:
        return False

@user_passes_test(testpermission)
def change_ctg(request):
    return HttpResponse("Now Y have permissions")


@permission_required("myapp.can_change_category")
def store_creator(request):
    return HttpResponse("Y have permissions")


class ProductListView(PermissionRequiredMixin, ListView):
    permission_required = "myapp.can_change_category"
    template_name = 'product.html'
    model = Product
