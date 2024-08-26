from django.urls import path
from . import views

app_name = "homepage"
urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("fleet/", views.fleet, name="fleet"),
    path("advantage/", views.advantage, name="advantage"),
    path("career/", views.career, name="career"),
    path("blog/", views.blog, name="blog"),
    path("contact/", views.contact, name="contact"),
]