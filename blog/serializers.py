from .models import Post, Comment, BlogMeta, NavLink, Category
from .documents import PostDocument
from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .utils import persian_time


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True, many=True)
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["created_at"] = persian_time(data["created_at"])
        data["updated_at"] = persian_time(data["updated_at"])
        return data


    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'category', 'slug', 'created_at', 'updated_at']


class ReplyCommentSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["created_at"] = persian_time(data["created_at"])
        data["updated_at"] = persian_time(data["updated_at"])

        return data


    class Meta:
        model = Comment
        fields = ['id', 'name', 'content', 'post', 'reply_to', 'created_at', 'updated_at']


class CommentSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        replies = Comment.objects.filter(reply_to=data["id"])
        data["replies"] = ReplyCommentSerializer(replies, many=True).data
        data["created_at"] = persian_time(data["created_at"])

        return data


    class Meta:
        model = Comment
        fields = ['id', 'name', 'content', 'post', 'reply_to', 'created_at', 'updated_at']


class BlogMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogMeta
        fields = ['meta']


class NavLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavLink
        fields = ['id', 'name', 'link']


class PostDocumentSerializer(DocumentSerializer):
    class Meta:
        document = PostDocument
        fields = (
            'id',
            'title',
            'content',
            'category',
            'slug',
            'created_at',
            'updated_at',
        )


class CustomPageSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["created_at"] = persian_time(data["created_at"])
        data["updated_at"] = persian_time(data["updated_at"])
        return data


    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'slug', 'created_at', 'updated_at']
