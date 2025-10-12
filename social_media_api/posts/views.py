from rest_framework import viewsets, permissions, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.contenttypes.models import ContentType
from django_filters import rest_framework as filters
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from notifications.models import Notification

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow authors of a post/comment to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to the author
        return obj.author == request.user

class PostFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    content = filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Post
        fields = ['title', 'content']

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = PostFilter
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['get'])
    def like_status(self, request, pk=None):
        """Get the like status and count for a post"""
        post = self.get_object()
        return Response({
            'likes_count': post.likes.count(),
            'has_liked': post.likes.filter(user=request.user).exists() if request.user.is_authenticated else False
        })
    
    @action(detail=True, methods=['get'])
    def comments(self, request, pk=None):
        post = self.get_object()
        comments = Comment.objects.filter(post=post)
        page = self.paginate_queryset(comments)
        
        if page is not None:
            serializer = CommentSerializer(page, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)
        
        serializer = CommentSerializer(comments, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        """Like or unlike a post"""
        post = generics.get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        
        if not created:
            # User already liked the post, so unlike it
            like.delete()
            return Response({'status': 'unliked'}, status=HTTP_204_NO_CONTENT)
        
        # Create notification for the post author
        if request.user != post.author:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='like',
                target_ct=ContentType.objects.get_for_model(post),
                target_id=post.id
            )
        
        serializer = LikeSerializer(like, context={'request': request})
        return Response(serializer.data, status=HTTP_201_CREATED)
            return self.get_paginated_response(serializer.data)
        
        serializer = CommentSerializer(comments, many=True, context={'request': request})
        return Response(serializer.data)
        
    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user
        
        # Check if the user has already liked the post
        like, created = Like.objects.get_or_create(user=user, post=post)
        
        if created:
            # Create notification for the post author
            if post.author != user:
                Notification.objects.create(
                    recipient=post.author,
                    actor=user,
                    verb='like',
                    target_ct=ContentType.objects.get_for_model(post),
                    target_id=post.id
                )
            return Response(LikeSerializer(like, context={'request': request}).data, 
                          status=HTTP_201_CREATED)
        return Response({'detail': 'You have already liked this post'})
        
    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        post = self.get_object()
        user = request.user
        
        try:
            like = Like.objects.get(user=user, post=post)
            like.delete()
            return Response(status=HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            return Response({'detail': 'You have not liked this post'})

    @action(detail=False, methods=['get'])
    def feed(self, request):
        """
        Return posts from users that the current user follows,
        ordered by creation date (newest first).
        """
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        page = self.paginate_queryset(posts)
        
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
            
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    
    def get_queryset(self):
        queryset = Comment.objects.all()
        if 'post_pk' in self.kwargs:
            return queryset.filter(post_id=self.kwargs['post_pk'])
        return queryset
    
    def perform_create(self, serializer):
        post = generics.get_object_or_404(Post, pk=self.kwargs['post_pk'])
        serializer.save(author=self.request.user, post=post)
