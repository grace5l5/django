import requests
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # This is similar to ones we have done before. Instead of keeping
    # the HTML / template in a separate directory, we just reply with
    # the HTML embedded here.
    return HttpResponse('''
        <h1>Welcome to my home page!</h1>
        <a href="/about-me">About</a> <br />
        <a href="/contact-me">Contact me</a> <br />
        <a href="/blogs">Blogs</a> <br />
        <a href="/projects">Projects</a> <br />
        <a href="/github-api-example">See my GitHub contributions</a> <br />
    ''')


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
    content_html = open("content/contact.html")
    context = {
        "content": content_html
    }
    return render(request, "base.html", context)


def blogs(request):
    content_html = open("content/blogs.html")
    context = {
        "content": content_html
    }
    return render(request, "base.html", context)


def projects(request):
    content_html = open("content/projects.html")
    context = {
        "content": content_html
    }
    return render(request, "base.html", context)


def github_api_example(request):
    # We can also combine Django with APIs
    response = requests.get('https://api.github.com/users/michaelpb/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, "github.html", context)

