from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'username', 'content', 'created_datetime']
        read_only_fields = ['id', 'created_datetime']

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many = True, read_only = True)

    class Meta:
        model = Post
        fields = ['id', 'username', 'created_datetime', 'title', 'content', 'comments']
        read_only_fields = ['id', 'created_datetime']
