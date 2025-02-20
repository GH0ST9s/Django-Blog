from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        "author": "Sushan Shrestha",
        "title": "Blog Post 1",
        "content": "First blog post",
        "datePosted": "February 20, 2025"
    },
    {
        "author": "Sushan Shrestha",
        "title": "Blog Post 2",
        "content": "Second blog post",
        "datePosted": "February 21, 2025"
    }
]

def home(request):
    context = {
        "title": "Home",
        "posts": posts,
    }
    return render(request, "blog/home.html", context)

def about(request):
    return render(request, "blog/about.html", {"title": "About"})
