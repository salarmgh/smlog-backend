from .models import Post, Comment
from rest_framework import serializers
from pprint import pprint


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
        pprint(data)
        replies = Comment.objects.filter(reply_to=data["id"])
        data["replies"] = ReplyCommentSerializer(replies, many=True).data

        return data

    class Meta:
        model = Comment
        fields = ['id', 'name', 'content', 'post', 'reply_to', 'created_at', 'updated_at']
