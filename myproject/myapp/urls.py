from django.urls import path
from .views import my_view

urlpatterns = [
    path("person/", my_view, name="my_view")
]
