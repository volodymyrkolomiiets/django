from django.urls import path
from .views import my_view

urlpatterns = [
    path("db/", my_view, name="my_view")
]
