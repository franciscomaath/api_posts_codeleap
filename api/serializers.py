from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'created_datetime']
        read_only_fields = ['id', 'created_datetime']

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many = True, read_only = True)
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['id', 'author', 'created_datetime', 'title', 'content', 'comments']
        read_only_fields = ['id', 'created_datetime']
