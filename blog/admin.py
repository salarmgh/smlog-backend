from django.contrib import admin
from django.forms import ModelForm, CharField
from tinymce.widgets import TinyMCE
from .models import Post, Comment, BlogMeta, NavLink, Category, CustomPage



class PostForm(ModelForm):
    content = CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 10}))

    class Meta:
        model = Post
        fields = ['title', 'content', 'category']


class PostAdmin(admin.ModelAdmin):
    form = PostForm


class PageForm(ModelForm):
    content = CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 10}))

    class Meta:
        model = CustomPage
        fields = ['title', 'content', 'slug']


class PageAdmin(admin.ModelAdmin):
    form = PageForm


admin.site.register(Post, PostAdmin)
admin.site.register(CustomPage, PageAdmin)
admin.site.register(Comment)
admin.site.register(BlogMeta)
admin.site.register(NavLink)
admin.site.register(Category)
