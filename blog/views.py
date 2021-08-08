from rest_framework import viewsets, generics
from .serializers import PostSerializer
from .models import Post


class PostViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "slug"
