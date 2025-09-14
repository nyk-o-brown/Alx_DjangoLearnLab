# DELETE Operation - Book Model

## Command
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

## Expected Output
```
Number of books remaining: 0
All books: []
```

## Alternative Method (Single Query Delete)
```python
from bookshelf.models import Book

# Delete using filter and delete method
Book.objects.filter(title="Nineteen Eighty-Four").delete()

# Verify deletion
remaining_books = Book.objects.all()
print(f"Books remaining: {remaining_books.count()}")
```

## Explanation
This command deletes a Book instance from the database. The process involves:
1. Retrieving the book object to be deleted
2. Calling the `delete()` method on the object
3. Confirming deletion by checking the database state

The `delete()` method removes the record from the database permanently. After deletion:
- The book object still exists in Python memory but is no longer in the database
- The primary key (ID) is freed and can be reused by future records
- All references to the deleted object become invalid

The confirmation step demonstrates that the book has been successfully removed by showing an empty queryset when retrieving all books.
