from django.shortcuts import render

from .models import Post


def home(request):
    """query all posts from the database"""
    posts = Post.objects.all().order_by("id")
    context = {
        "posts": posts
    }
    return render(request, "posts/home.html", context)
