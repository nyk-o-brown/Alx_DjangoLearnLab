# UPDATE Operation - Book Model

## Command
```python
from bookshelf.models import Book

# Update the title of "1984" to "Nineteen Eighty-Four" and save the changes
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Verify the update
print(f"Updated title: {book.title}")
```

## Expected Output
```
Updated title: Nineteen Eighty-Four
```

## Alternative Method (Single Query Update)
```python
from bookshelf.models import Book

# Update using filter and update method (more efficient for bulk updates)
Book.objects.filter(title="1984").update(title="Nineteen Eighty-Four")

# Verify the update
updated_book = Book.objects.get(title="Nineteen Eighty-Four")
print(f"Updated title: {updated_book.title}")
```

## Explanation
This command updates an existing Book instance in the database. The process involves:
1. Retrieving the book object using `Book.objects.get()`
2. Modifying the desired attribute (title in this case)
3. Calling `save()` to persist the changes to the database

The `save()` method updates the existing record rather than creating a new one, maintaining the same primary key and other unchanged fields.

The alternative method using `filter().update()` is more efficient for bulk updates as it executes a single SQL UPDATE statement.
