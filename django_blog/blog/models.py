from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class Post(models.Model):
    """
    Model representing a blog post.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    
    # Additional fields for enhanced blog functionality
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10,
        choices=[
            ('draft', 'Draft'),
            ('published', 'Published')
        ],
        default='draft'
    )
    
    class Meta:
        ordering = ['-published_date']
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        """Returns the URL to access a detailed record for this post."""
        return reverse('post-detail', args=[str(self.id)])
    
    def publish(self):
        """Publish the blog post."""
        self.published_date = timezone.now()
        self.status = 'published'
        self.save()

class Comment(models.Model):
    """
    Model representing a comment on a blog post.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['created_date']
        
    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
    
    def approve(self):
        """Approve the comment."""
        self.approved = True
        self.save()

class Category(models.Model):
    """
    Model representing a blog post category.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    posts = models.ManyToManyField(Post, related_name='categories', blank=True)
    
    class Meta:
        verbose_name_plural = "categories"
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        """Returns the URL to access a list of posts in this category."""
        return reverse('category-detail', args=[str(self.id)])
