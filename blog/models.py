from django.db import models
from django.utils.text import slugify


class Post(models.Model):
    title = models.TextField()
    content = models.TextField()
    slug = models.SlugField(allow_unicode=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reply_to = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class BlogMeta(models.Model):
    meta = models.JSONField()


class NavLink(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=255)
