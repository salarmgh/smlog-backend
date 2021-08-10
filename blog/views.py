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


class CommentViewSet(viewsets.ViewSet, generics.ListAPIView):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer


class PostCommentViewSet(viewsets.ViewSet, generics.ListAPIView):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    serializer_class = CommentSerializer
    lookup_url_kwarg = "post"

    def get_queryset(self):
        post_id = self.kwargs.get(self.lookup_url_kwarg)
        post = Post.objects.get(pk=post_id)
        queryset = Comment.objects.filter(post=post.id)
        return queryset

class CreateCommentViewSet(viewsets.ViewSet, generics.CreateAPIView):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    model = Comment
    serializer_class = CommentSerializer
    queryset = Comment.objects.all().order_by('-created_at')
