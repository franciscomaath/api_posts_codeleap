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

    likes_count = serializers.SerializerMethodField()
    liked_by_users = serializers.StringRelatedField(source='likes', many = True, read_only = True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'created_datetime', 'title', 'content', 'comments', 'likes_count', 'liked_by_users']
        read_only_fields = ['id', 'created_datetime']

    def get_likes_count(self, obj):
        return obj.likes.count()
