import requests
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    content_html = open("content/index.html").read()
    context = {
        "content": content_html
    }
    return render(request, "base.html", context)


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
    content_html = open("content/contact.html").read()
    context = {
        "content": content_html
    }
    return render(request, "base.html", context)


def blogs(request):
    content_html = open("content/blogs.html").read()
    context = {
        "content": content_html
    }
    return render(request, "base.html", context)


def projects(request):
    content_html = open("content/projects.html").read()
    context = {
        "content": content_html,
    }
    return render(request, "base.html", context)


def github_api_example(request):
    # We can also combine Django with APIs
    response = requests.get('https://api.github.com/users/grace5l5/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, "github.html", context)

