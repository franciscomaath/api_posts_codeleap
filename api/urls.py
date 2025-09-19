from django.urls import path
from .views import PostList, PostDetail, CommentCreateView, PostLikeView

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('<int:post_pk>/comments/', CommentCreateView.as_view(), name='comment-create'),
    path('<int:pk>/like/', PostLikeView.as_view(), name='post-like'),
]