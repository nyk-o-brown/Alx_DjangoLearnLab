from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework as filters
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class BookFilter(filters.FilterSet):
    """
    FilterSet for Book model to enable advanced filtering capabilities.
    Allows filtering books by title, publication year, and author name.
    """
    title = filters.CharFilter(lookup_expr='icontains')
    min_year = filters.NumberFilter(field_name='publication_year', lookup_expr='gte')
    max_year = filters.NumberFilter(field_name='publication_year', lookup_expr='lte')
    author_name = filters.CharFilter(field_name='author__name', lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

class BookList(generics.ListCreateAPIView):
    """
    List all books or create a new book.
    
    GET: Retrieve a list of all books
    POST: Create a new book
    
    Permissions:
    - List: Allow any user to view the list
    - Create: Only authenticated users can create new books
    
    Filtering:
    - Supports filtering by title, publication year range, and author name
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BookFilter

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a book instance.
    
    GET: Retrieve a specific book by ID
    PUT/PATCH: Update a specific book
    DELETE: Remove a specific book
    
    Permissions:
    - Retrieve: Allow any user to view details
    - Update/Delete: Only authenticated users can modify or remove books
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class AuthorList(generics.ListCreateAPIView):
    """
    List all authors or create a new author.
    
    GET: Retrieve a list of all authors
    POST: Create a new author
    
    Permissions:
    - List: Allow any user to view the list
    - Create: Only authenticated users can create new authors
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an author instance.
    
    GET: Retrieve a specific author by ID
    PUT/PATCH: Update a specific author
    DELETE: Remove a specific author
    
    Permissions:
    - Retrieve: Allow any user to view details
    - Update/Delete: Only authenticated users can modify or remove authors
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookListView(ListView):
    model = Book
    template_name = 'api/book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'api/book_detail.html'

class BookCreateView(CreateView):
    model = Book
    template_name = 'api/book_form.html'
    fields = ['title', 'publication_year', 'author']

class BookUpdateView(UpdateView):
    model = Book
    template_name = 'api/book_form.html'
    fields = ['title', 'publication_year', 'author']

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'api/book_confirm_delete.html'
    success_url = '/books/'