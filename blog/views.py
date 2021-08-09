from rest_framework import viewsets, generics
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment


class PostViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    lookup_field = "slug"


class CommentViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Comment.objects.filter(reply_to=None)
    serializer_class = CommentSerializer
