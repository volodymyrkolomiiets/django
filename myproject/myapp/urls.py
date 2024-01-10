from django.urls import path
from .views import index, my_view, about


urlpatterns = [
    path("index/<str:name>/", index),
    path("my_view/<str:name>/", my_view),
    path("about/", about)
]