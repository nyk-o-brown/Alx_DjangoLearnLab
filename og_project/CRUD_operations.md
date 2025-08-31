# CRUD Operations for Book Model - Django ORM

This document demonstrates all CRUD (Create, Read, Update, Delete) operations for the Book model using Django's ORM.

## Prerequisites
- Django project with bookshelf app configured
- Book model migrated to database
- Django shell access

## 1. CREATE Operation

### Command
```python
from bookshelf.models import Book

# Create a Book instance with title "1984", author "George Orwell", and publication year 1949
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
```

### Expected Output
```
<Book: 1984 by George Orwell (1949)>
```

### Explanation
Creates a new Book instance and automatically saves it to the database. Returns the created object.

---

## 2. RETRIEVE Operation

### Command
```python
from bookshelf.models import Book

# Retrieve and display all attributes of the book you just created
book = Book.objects.get(title="1984")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")
print(f"ID: {book.id}")
```

### Expected Output
```
Title: 1984
Author: George Orwell
Publication Year: 1949
ID: 1
```

### Alternative Retrieval Methods
```python
# Get all books
all_books = Book.objects.all()

# Filter books by author
orwell_books = Book.objects.filter(author="George Orwell")

# Get book by ID
book = Book.objects.get(id=1)
```

---

## 3. UPDATE Operation

### Command
```python
from bookshelf.models import Book

# Update the title of "1984" to "Nineteen Eighty-Four" and save the changes
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Verify the update
print(f"Updated title: {book.title}")
```

### Expected Output
```
Updated title: Nineteen Eighty-Four
```

### Alternative Update Method
```python
# Single query update (more efficient)
Book.objects.filter(title="1984").update(title="Nineteen Eighty-Four")
```

---

## 4. DELETE Operation

### Command
```python
from bookshelf.models import Book

# Delete the book you created and confirm the deletion
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion by trying to retrieve all books
all_books = Book.objects.all()
print(f"Number of books remaining: {all_books.count()}")
print("All books:", list(all_books))
```

### Expected Output
```
Number of books remaining: 0
All books: []
```

### Alternative Delete Method
```python
# Single query delete
Book.objects.filter(title="Nineteen Eighty-Four").delete()
```

---

## Complete CRUD Session Example

Here's a complete session demonstrating all operations in sequence:

```python
# Start Django shell: python manage.py shell

from bookshelf.models import Book

# CREATE
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(f"Created: {book}")

# READ
retrieved_book = Book.objects.get(title="1984")
print(f"Retrieved: {retrieved_book.title} by {retrieved_book.author}")

# UPDATE
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
print(f"Updated title: {retrieved_book.title}")

# DELETE
retrieved_book.delete()
print(f"Books remaining: {Book.objects.count()}")
```

## Model Definition Reference

The Book model used in these operations:

```python
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    
    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
```

## Key Django ORM Concepts Demonstrated

1. **Object Creation**: `Model.objects.create()` method
2. **Object Retrieval**: `Model.objects.get()` and `Model.objects.filter()` methods
3. **Object Updates**: Modifying attributes and calling `save()` method
4. **Object Deletion**: `delete()` method on model instances
5. **QuerySets**: Django's lazy evaluation of database queries
6. **Model Methods**: Custom `__str__` method for string representation

## Database Verification

After each operation, you can verify the database state using:
```python
# Check all books
Book.objects.all()

# Check count
Book.objects.count()

# Check specific book
Book.objects.filter(title="1984").exists()
```
