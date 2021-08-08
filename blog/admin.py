from django.contrib import admin
from django.forms import ModelForm
from .models import Post


class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'content']


admin.site.register(Post, PostAdmin)
