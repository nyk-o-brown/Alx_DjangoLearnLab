from django.test import TestCase
from .models import Book


class BookModelTest(TestCase):
    """Test cases for the Book model."""
    
    def test_book_creation(self):
        """Test that a book can be created with valid data."""
        book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            publication_year=2023
        )
        self.assertEqual(book.title, "Test Book")
        self.assertEqual(book.author, "Test Author")
        self.assertEqual(book.publication_year, 2023)
    
    def test_book_string_representation(self):
        """Test the string representation of the Book model."""
        book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            publication_year=2023
        )
        expected_string = "Test Book by Test Author (2023)"
        self.assertEqual(str(book), expected_string)
