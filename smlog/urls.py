"""smlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
import debug_toolbar
from blog import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'page', views.CustomPageViewSet)
router.register(r'comment', views.CreateCommentViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'meta', views.BlogMetaViewSet)
router.register(r'nav-links', views.NavLinkViewSet)
router.register(r'comments/(?P<post>[^/.]+)', views.PostCommentViewSet, basename="post-comments")
router.register(r'category/(?P<name>[^/.]+)', views.PostCategoryViewSet, basename="category-posts")
router.register(
    prefix=r'search',
    basename='posts_documents',
    viewset=views.PostDocumentViewSet
)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
]
