from django.urls import path
from .views import index, my_view, about, myview, menu, menu_by_id


urlpatterns = [
    path("index/<str:name>/", index),
    path("my_view/<str:name>/", my_view),
    path("about/", about),
    path("myview/", myview),
    path("menu/", menu),
    path("menu_card/", menu_by_id)
]