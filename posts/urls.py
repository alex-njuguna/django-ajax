from django.urls import path

from . import views

app_name = "posts"
urlpatterns = [
    path("", views.home, name="home"),
    path("data/<int:num_posts>/", views.load_posts_data, name="load_posts_data"),
    path("like_unlike_post", views.like_unlike_post, name="like_unlike_post"),
]