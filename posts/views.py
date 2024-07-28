from django.shortcuts import render
from django.http import JsonResponse

from .models import Post


def home(request):
    """query all posts from the database"""
    posts = Post.objects.all().order_by("id")
    context = {
        "posts": posts
    }
    return render(request, "posts/home.html", context)

def load_posts_data(request, num_posts):
    visible = 3
    upper = num_posts
    lower = upper - visible
    size = Post.objects.all().count()

    posts = Post.objects.all().order_by("-liked")
    data = []
    for post in posts:
        a_post = {
            "id": post.id,
            "title": post.title,
            "body": post.body,
            "liked": True if request.user in post.liked.all() else False,
            "count": post.like_count,
            "author": post.author.user.username,
        }
        data.append(a_post)
        
    context = {
        "data": data[lower:upper],
        "size": size
    }

    return JsonResponse(context)

def like_unlike_post(request):
    """Add or remove a user to the liked post column"""
    if request.is_ajax():
        pk = request.POST.get("pk")
        post = Post.objects.get(pk=pk)
        if request.user in post.liked.all():
            liked = False
            post.liked.remove(request.user)
        else:
            liked = True
            post.liked.add(request.user)

    context = {
        "liked": liked,
        "count": post.like_count
    }

    return JsonResponse(context)
