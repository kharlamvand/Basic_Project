from django.urls import path
from .import views

urlpatterns = [
    path("", views.projects, name="projects"),
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("services/", views.services, name="services"),
    path("projects-detail/", views.projects_detail, name="projects-detail"),


]
