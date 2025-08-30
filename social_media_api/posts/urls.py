 from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, feed, like_post, unlike_post

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', feed, name='feed'),
    path('<int:pk>/like/', LikePostView.as_view(), name='like-post'),
path('<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
] 