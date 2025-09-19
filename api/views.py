from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from django.http import Http404
from rest_framework.pagination import PageNumberPagination

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django.shortcuts import get_object_or_404

# Create your views here.
class PostList(APIView):
    def get(self, request, format=None):
        posts = Post.objects.all()

        # filtering and ordering
        search_filter = filters.SearchFilter()
        ordering_filter = filters.OrderingFilter()

        self.search_fields = ['title', 'content']
        self.ordering_fields = ['created_datetime', 'title']

        # read '?search=' and '?ordering=' from URL
        filtered_posts = search_filter.filter_queryset(request, posts, self)
        ordered_posts = search_filter.filter_queryset(request, filtered_posts, self)

        # pagination
        paginator = PageNumberPagination()
        paginated_posts = paginator.paginate_queryset(ordered_posts, request, view=self)

        if paginated_posts is not None:
            serializer = PostSerializer(paginated_posts, many = True)
            return paginator.get_paginated_response(serializer.data)

        # return empty list if page is empty
        serializer = PostSerializer(posts, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author = request.user)
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

class PostLikeView(APIView):
    def post(self, request, pk, format = None):
        post = get_object_or_404(Post, pk=pk)
        user = request.user

        if post.likes.filter(pk = user.pk).exists():
            post.likes.remove(user)
            message = 'Post unliked successfully.'
        else:
            post.likes.add(user)
            message = 'Post liked successfully.'
        
        return Response({"detail": message}, status = status.HTTP_200_OK)


class CommentCreateView(APIView):
    def post(self, request, post_pk, format = None):
        post = get_object_or_404(Post, pk=post_pk)
        serializer = CommentSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save(post = post, author = request.user)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) 
