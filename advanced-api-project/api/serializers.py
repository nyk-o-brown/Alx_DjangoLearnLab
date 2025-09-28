from rest_framework import serializers
from django.utils import timezone
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    
    This serializer handles the conversion of Book model instances to JSON format
    and vice versa. It includes custom validation for the publication_year field
    to ensure it's not in the future.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """
        Custom validation to ensure publication_year is not in the future.
        
        Args:
            value: The publication year to validate.
            
        Returns:
            The validated year if it's valid.
            
        Raises:
            serializers.ValidationError: If the year is in the future.
        """
        if value > timezone.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    
    This serializer provides a nested representation of an author's books,
    making it easy to access all books by an author in API responses.
    The nested books are read-only to prevent circular dependencies in creation.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']