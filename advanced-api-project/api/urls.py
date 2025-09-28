from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    # API endpoints using DRF views
    path('books/', views.BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetail.as_view(), name='book-detail'),
    path('authors/', views.AuthorList.as_view(), name='author-list'),
    path('authors/<int:pk>/', views.AuthorDetail.as_view(), name='author-detail'),

    # Traditional Django views for web interface
    path('books/list/', views.BookListView.as_view(), name='book-list-view'),
    path('books/<int:pk>/detail/', views.BookDetailView.as_view(), name='book-detail-view'),
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),
    path('books/update/', views.BookUpdateView.as_view(), name='book-update'),
    path('books/delete/', views.BookDeleteView.as_view(), name='book-delete'),
]