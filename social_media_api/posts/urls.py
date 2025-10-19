from rest_framework_nested import routers
from django.urls import path, include
from .views import PostViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r'', PostViewSet, basename='post')

posts_router = routers.NestedDefaultRouter(router, r'', lookup='post')
posts_router.register(r'comments', CommentViewSet, basename='post-comments')

app_name = 'posts'

urlpatterns = [
    path('', include(router.urls)),
    path('', include(posts_router.urls)),
]  