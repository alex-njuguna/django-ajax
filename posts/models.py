"""
Post - author, title, body, liked, created, updated
"""
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

from profiles.models import Profile


class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=300, unique=True, blank=True)
    body = models.TextField()
    liked = models.ManyToManyField(User, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.title)
