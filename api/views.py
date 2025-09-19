from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.pagination import PageNumberPagination

from .models import Post
from .serializers import PostSerializer

# Create your views here.
class PostList(APIView):
    def get(self, request, format=None):
        posts = Post.objects.all()
        paginator = PageNumberPagination()
        paginated_posts = paginator.paginate_queryset(posts, request, view=self)
        serializer = PostSerializer(posts, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class PostDetail(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk = pk)
        except Post.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def patch(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
    