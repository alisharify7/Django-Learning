from django.urls import path

from .views import index, show_posts


urlpatterns = [
    path("",index, name="index"),
    path("show/",show_posts ,name="show posts")
]