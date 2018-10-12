import requests
from django.shortcuts import render


def index(request):
    context = {}
    return render(request, "index.html", context)


def contact_me(request):
    context = {}
    return render(request, "contact.html", context)


def blogs(request):
    context = {}
    return render(request, "blogs.html", context)


def projects(request):
    response = requests.get('https://api.github.com/users/grace5l5/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, "projects.html", context)
