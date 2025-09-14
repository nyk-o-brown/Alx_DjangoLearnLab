import profile
from django.contrib.auth.models import BaseUserManager
from django.db import models

from advanced_features_and_security.LibraryProject.relationship_app.models import CustomUserManager


class Book(models.Model):
    """
    Book model representing a book in the bookshelf.
    
    Fields:
        title: The title of the book (max 200 characters)
        author: The author of the book (max 100 characters)
        publication_year: The year the book was published
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    
    def __str__(self):
        """String representation of the Book model."""
        return f"{self.title} by {self.author} ({self.publication_year})"
    
    class Meta:
        """Meta options for the Book model."""
        ordering = ['title']


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def Create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)


    def CustomeUser(AbstractUser):
        email = models.EmailField(unique=True)
        date_of_birth = models.DateField(null=True, blank=True)
        profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

        objects =CustomUserManager()

        def __str__(self):
            return self.username


