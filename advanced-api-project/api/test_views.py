from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Author, Book
from .serializers import BookSerializer, AuthorSerializer
from django.utils import timezone

class APIBaseTestCase(APITestCase):
    """Base test case class for API tests with common setup."""
    
    def setUp(self):
        """Set up test data and authentication."""
        # Create test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
        # Create test authors
        self.author1 = Author.objects.create(name='John Smith')
        self.author2 = Author.objects.create(name='Jane Doe')
        
        # Create test books
        self.book1 = Book.objects.create(
            title='Python Testing',
            publication_year=2023,
            author=self.author1
        )
        self.book2 = Book.objects.create(
            title='Django REST APIs',
            publication_year=2022,
            author=self.author1
        )
        self.book3 = Book.objects.create(
            title='JavaScript Basics',
            publication_year=2021,
            author=self.author2
        )
        
        # Set up API client
        self.client = APIClient()
        
        # URLs
        self.book_list_url = reverse('book-list')
        self.author_list_url = reverse('author-list')
        self.book_detail_url = lambda pk: reverse('book-detail', args=[pk])
        self.author_detail_url = lambda pk: reverse('author-detail', args=[pk])

    def authenticate(self):
        """Helper method to authenticate requests."""
        self.client.force_authenticate(user=self.user)

class BookCRUDTests(APIBaseTestCase):
    """Test CRUD operations for Book endpoints."""

    def test_create_book(self):
        """Test creating a new book."""
        self.authenticate()
        data = {
            'title': 'New Book',
            'publication_year': 2024,
            'author': self.author1.id
        }
        response = self.client.post(self.book_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)
        self.assertEqual(Book.objects.get(title='New Book').author, self.author1)

    def test_create_book_unauthenticated(self):
        """Test that unauthenticated users cannot create books."""
        data = {
            'title': 'Unauthorized Book',
            'publication_year': 2024,
            'author': self.author1.id
        }
        response = self.client.post(self.book_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Book.objects.count(), 3)  # No new book created

    def test_get_book_list(self):
        """Test retrieving list of books."""
        response = self.client.get(self.book_list_url)
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], serializer.data)  # Assuming pagination is enabled

    def test_get_book_detail(self):
        """Test retrieving a specific book."""
        response = self.client.get(self.book_detail_url(self.book1.id))
        serializer = BookSerializer(self.book1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_book(self):
        """Test updating a book."""
        self.authenticate()
        data = {
            'title': 'Updated Python Testing',
            'publication_year': 2024,
            'author': self.author2.id
        }
        response = self.client.put(self.book_detail_url(self.book1.id), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Python Testing')
        self.assertEqual(self.book1.author, self.author2)

    def test_delete_book(self):
        """Test deleting a book."""
        self.authenticate()
        response = self.client.delete(self.book_detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2)

class BookFilterSearchTests(APIBaseTestCase):
    """Test filtering, searching, and ordering for Book endpoints."""

    def test_filter_by_title(self):
        """Test filtering books by title."""
        response = self.client.get(f"{self.book_list_url}?title=Python")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], 'Python Testing')

    def test_filter_by_year_range(self):
        """Test filtering books by publication year range."""
        response = self.client.get(f"{self.book_list_url}?min_year=2022")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)  # Should return 2 books (2022 and 2023)

    def test_search_functionality(self):
        """Test search functionality across title and author name."""
        response = self.client.get(f"{self.book_list_url}?search=John")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)  # Should return John Smith's books

    def test_ordering(self):
        """Test ordering of books."""
        # Test ascending order by title
        response = self.client.get(f"{self.book_list_url}?ordering=title")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [book['title'] for book in response.data['results']]
        self.assertEqual(titles, sorted(titles))

        # Test descending order by publication year
        response = self.client.get(f"{self.book_list_url}?ordering=-publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data['results']]
        self.assertEqual(years, sorted(years, reverse=True))

class AuthorTests(APIBaseTestCase):
    """Test Author endpoints."""

    def test_create_author(self):
        """Test creating a new author."""
        self.authenticate()
        data = {'name': 'New Author'}
        response = self.client.post(self.author_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 3)

    def test_get_author_list(self):
        """Test retrieving list of authors."""
        response = self.client.get(self.author_list_url)
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], serializer.data)  # Assuming pagination is enabled

    def test_search_authors(self):
        """Test searching authors by name."""
        response = self.client.get(f"{self.author_list_url}?search=John")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['name'], 'John Smith')