import requests
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {}
    return render(request, "index.html", context)


def about_me(request):
    # Django comes with a "shortcut" function called "render", that
    # lets us read in HTML template files in separate directories to
    # keep our code better organized.
    context = {
        'name': 'Ash Ketchum',
        'pokemon': 'Pikachu',
    }
    return render(request, "about_me.html", context)


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


