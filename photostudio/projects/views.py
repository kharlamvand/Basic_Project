from django.shortcuts import render, redirect


def projects(request):
    return render(request, "projects/projects.html")


def home(request):
    return render(request, "projects/index.html")


def about(request):
    return render(request, "projects/about.html")


def contact(request):
    return render(request, "projects/contact.html")


def services(request):
    return render(request, "projects/services.html")


def projects_detail(request):
    return render(request, "projects/projects-detail.html")
