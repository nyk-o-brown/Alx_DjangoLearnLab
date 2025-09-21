from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from .models import Book
from .serializers import BookSerializer

# Create your views here.

class BookList(generics.ListAPIView):
    """
    Public view - allows anyone to read the list of books
    No authentication required for this view
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Allow public access

class BookViewSet(viewsets.ModelViewSet):
    """
    Protected view - requires authentication for all CRUD operations
    Only authenticated users can create, read, update, or delete books
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Require authentication
