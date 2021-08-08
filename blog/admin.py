from django.contrib import admin
from django.forms import ModelForm
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'content']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
