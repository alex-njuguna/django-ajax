from django.urls import path

from . import views

app_name = "posts"
urlpatterns = [
    path("", views.home, name="home"),
    path("test_ajax/", views.test_ajax, name="test_ajax"),
    path("data/<int:num_posts>/", views.load_posts_data, name="load_posts_data"),
]