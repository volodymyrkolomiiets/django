
from django.urls import path
from .views import my_view, index, change_ctg, store_creator, ProductListView

urlpatterns = [
    path("my_view/", my_view ),
    path("index/", index ),
    path("change_ctg/", change_ctg),
    path("store/", store_creator),
    path("products/", ProductListView.as_view())
]
