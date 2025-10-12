from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Custom user model that extends Django's AbstractUser.
    Adds additional fields for user profile functionality.
    """
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    followers = models.ManyToManyField(
        'self',
        related_name='following',
        symmetrical=False,
        blank=True
    )
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date_joined']
    
    def __str__(self):
        return self.username
    
    @property
    def follower_count(self):
        """Returns the number of followers"""
        return self.followers.count()
    
    @property
    def following_count(self):
        """Returns the number of users this user is following"""
        return self.following.count()
    
    def follow(self, user):
        """Follow the specified user"""
        if user != self:
            user.followers.add(self)
    
    def unfollow(self, user):
        """Unfollow the specified user"""
        if user != self:
            user.followers.remove(self)
    
    def is_following(self, user):
        """Check if the current user is following the specified user"""
        return self.following.filter(id=user.id).exists()
