# CREATE Operation - Book Model

## Command
```python
from bookshelf.models import Book

# Create a Book instance with title "1984", author "George Orwell", and publication year 1949
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
```

## Expected Output
```
<Book: 1984 by George Orwell (1949)>
```

## Explanation
This command creates a new Book instance in the database with the specified attributes:
- title: "1984" (CharField, max 200 characters)
- author: "George Orwell" (CharField, max 100 characters)  
- publication_year: 1949 (IntegerField)

The `Book.objects.create()` method automatically saves the object to the database and returns the created instance. The string representation shows the book's title, author, and publication year as defined in the `__str__` method of the Book model.
