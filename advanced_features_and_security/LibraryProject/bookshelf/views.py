from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import permission_required


@permission_required('books.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    # logic to edit the book
    return render(request, 'edit_book.html', {'book': book})


def book_list(request):
    """View to display a list of all books."""
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


def book_detail(request, book_id):
    """View to display details of a specific book."""
    try:
        book = Book.objects.get(id=book_id)
        return render(request, 'bookshelf/book_detail.html', {'book': book})
    except Book.DoesNotExist:
        return render(request, 'bookshelf/book_not_found.html', status=404)


def edit_book()        
