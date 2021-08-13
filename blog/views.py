from rest_framework import viewsets, generics
from rest_framework.response import Response
from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_RANGE,
    LOOKUP_QUERY_IN,
    LOOKUP_QUERY_GT,
    LOOKUP_QUERY_GTE,
    LOOKUP_QUERY_LT,
    LOOKUP_QUERY_LTE,
)
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
    DefaultOrderingFilterBackend,
    SearchFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from .serializers import PostSerializer, CommentSerializer, BlogMetaSerializer, NavLinkSerializer, PostDocumentSerializer, CategorySerializer, CustomPageSerializer
from .models import Post, Comment, BlogMeta, NavLink, Category, CustomPage
from .documents import PostDocument
from rest_framework.throttling import AnonRateThrottle

__all__ = (
    'BookSourceSearchBackendDocumentViewSet',
)


class PostViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    @method_decorator(cache_page(60*60*2))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    @method_decorator(cache_page(60*60*2))
    def list(self, *args, **kwargs):
        return super().list(*args, **kwargs)

    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    lookup_field = "slug"


class CustomPageViewSet(viewsets.ViewSet, generics.RetrieveAPIView):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    @method_decorator(cache_page(60*60*2))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    queryset = CustomPage.objects.all()
    serializer_class = CustomPageSerializer
    lookup_field = "slug"


class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    @method_decorator(cache_page(60*60*2))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    @method_decorator(cache_page(60*60*2))
    def list(self, *args, **kwargs):
        return super().list(*args, **kwargs)

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CommentViewSet(viewsets.ViewSet, generics.ListAPIView):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    @method_decorator(cache_page(60*60*2))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    @method_decorator(cache_page(60*60*2))
    def list(self, *args, **kwargs):
        return super().list(*args, **kwargs)

    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer


class PostCommentViewSet(viewsets.ViewSet, generics.ListAPIView):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    serializer_class = CommentSerializer
    lookup_url_kwarg = "post"

    @method_decorator(cache_page(60*60*2))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    @method_decorator(cache_page(60*60*2))
    def list(self, *args, **kwargs):
        return super().list(*args, **kwargs)

    def get_queryset(self):
        post_id = self.kwargs.get(self.lookup_url_kwarg)
        post = Post.objects.get(pk=post_id)
        queryset = Comment.objects.filter(post=post.id).filter(approve=True)
        return queryset

class CreateCommentViewSet(viewsets.ViewSet, generics.CreateAPIView):
    """
    API endpoint that allows posts to be viewed or edited.
    """

    model = Comment
    serializer_class = CommentSerializer
    queryset = Comment.objects.all().order_by('-created_at')

    throttle_classes = [AnonRateThrottle]


class BlogMetaViewSet(viewsets.ViewSet, generics.ListAPIView):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    model = BlogMeta
    serializer_class = BlogMetaSerializer
    queryset = BlogMeta.objects.all()

    @method_decorator(cache_page(60*60*2))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    @method_decorator(cache_page(60*60*2))
    def list(self, *args, **kwargs):
        return super().list(*args, **kwargs)


class NavLinkViewSet(viewsets.ViewSet, generics.ListAPIView):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    model = NavLink
    serializer_class = NavLinkSerializer
    queryset = NavLink.objects.all()

    @method_decorator(cache_page(60*60*2))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    @method_decorator(cache_page(60*60*2))
    def list(self, *args, **kwargs):
        return super().list(*args, **kwargs)

class PostCategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    serializer_class = PostSerializer
    lookup_url_kwarg = "name"

    @method_decorator(cache_page(60*60*2))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    @method_decorator(cache_page(60*60*2))
    def list(self, *args, **kwargs):
        return super().list(*args, **kwargs)

    def get_queryset(self):
        category_name = self.kwargs.get(self.lookup_url_kwarg)
        category = Category.objects.get(name=category_name)
        queryset = Post.objects.filter(category=category)
        return queryset


class PostDocumentViewSet(DocumentViewSet):
    document = PostDocument
    serializer_class = PostDocumentSerializer

    lookup_field = 'id'
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
    ]

    search_fields = (
        'title',
        'content',
    )

    filter_fields = {
        'id': {
            'field': 'id',
            'lookups': [
                LOOKUP_FILTER_RANGE,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_GT,
                LOOKUP_QUERY_GTE,
                LOOKUP_QUERY_LT,
                LOOKUP_QUERY_LTE,
            ],
        },
        'title': 'title.raw',
        'content': 'content.raw',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
    }

    ordering_fields = {
        'id': 'id',
        'title': 'title.raw',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
    }

    ordering = ('id', 'created_at',)
