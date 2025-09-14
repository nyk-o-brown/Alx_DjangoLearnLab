# RETRIEVE Operation - Book Model

## Command
```python
from bookshelf.models import Book

# Retrieve and display all attributes of the book you just created
book = Book.objects.get(title="1984")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")
print(f"ID: {book.id}")
```

## Expected Output
```
Title: 1984
Author: George Orwell
Publication Year: 1949
ID: 1
```

## Explanation
This command retrieves the Book instance from the database using the `Book.objects.get()` method with the title as a filter. The `get()` method returns a single object that matches the criteria.

Alternative retrieval methods:
- `Book.objects.all()` - retrieves all books
- `Book.objects.filter(author="George Orwell")` - retrieves books by author
- `Book.objects.get(id=1)` - retrieves book by primary key

The retrieved book object allows access to all model fields and methods defined in the Book model.
