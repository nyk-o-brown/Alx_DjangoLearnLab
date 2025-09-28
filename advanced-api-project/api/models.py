from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Author(models.Model):
    """
    Model representing a book author.
    
    This model stores basic information about authors and maintains
    a one-to-many relationship with the Book model through the related_name
    'books'.
    """
    name = models.CharField(max_length=200, help_text="Enter the author's name")
    
    def __str__(self):
        """String representation of the Author object."""
        return self.name

class Book(models.Model):
    """
    Model representing a book.
    
    This model stores information about books including their title,
    publication year, and the relationship to their author. It includes
    custom validation to ensure the publication year is not in the future.
    """
    title = models.CharField(max_length=200, help_text="Enter the book title")
    publication_year = models.IntegerField(help_text="Enter the year of publication")
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books',
        help_text="Select the book's author"
    )

    def clean(self):
        """
        Custom validation to ensure publication_year is not in the future.
        """
        if self.publication_year > timezone.now().year:
            raise ValidationError({
                'publication_year': 'Publication year cannot be in the future.'
            })

    def __str__(self):
        """String representation of the Book object."""
        return f"{self.title} ({self.publication_year}) by {self.author.name}"

    class Meta:
        ordering = ['-publication_year', 'title']