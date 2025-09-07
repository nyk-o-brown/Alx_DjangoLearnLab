# query_samples.py

import os
import django

# ✅ Setup Django environment (only needed if running standalone)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1️⃣ Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author) # uses related_name='books' from ForeignKey
        print(f"\nBooks by {author.name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")

# 2️⃣ List all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()  # ManyToManyField access
        print(f"\nBooks in {library.name}:")
        for book in books:
            print(f"- {book.title} by {book.author.name}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")

# 3️⃣ Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian  # OneToOneField reverse access
        print(f"\nLibrarian for {library.name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to '{library_name}'.")

# 🧪 Sample usage
if __name__ == "__main__":
    get_books_by_author("Chinua Achebe")
    get_books_in_library("Central Library")
    get_librarian_for_library("Central Library")
