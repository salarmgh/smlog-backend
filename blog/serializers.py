from .models import Post, Comment, BlogMeta, NavLink
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'slug', 'created_at', 'updated_at']


class ReplyCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'name', 'content', 'post', 'reply_to', 'created_at', 'updated_at']


class CommentSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        replies = Comment.objects.filter(reply_to=data["id"])
        data["replies"] = ReplyCommentSerializer(replies, many=True).data

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
