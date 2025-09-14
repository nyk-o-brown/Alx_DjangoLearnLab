#!/usr/bin/env python
"""
Test script to verify that relationship_app is properly configured and accessible.
"""

import os
import sys
import django

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

# Now we can import Django models
from relationship_app.models import Author, Book, Library, Librarian

def test_relationship_app():
    """Test that relationship_app models can be imported and used."""
    print("Testing relationship_app models...")
    
    # Test Author model
    print("✓ Author model imported successfully")
    
    # Test Book model
    print("✓ Book model imported successfully")
    
    # Test Library model
    print("✓ Library model imported successfully")
    
    # Test Librarian model
    print("✓ Librarian model imported successfully")
    
    # Test creating objects
    try:
        # Create an author
        author = Author.objects.create(name="Test Author")
        print(f"✓ Created author: {author.name}")
        
        # Create a book
        book = Book.objects.create(title="Test Book", author=author)
        print(f"✓ Created book: {book.title} by {book.author.name}")
        
        # Create a library
        library = Library.objects.create(name="Test Library")
        print(f"✓ Created library: {library.name}")
        
        # Add book to library
        library.books.add(book)
        print(f"✓ Added book to library")
        
        # Create a librarian
        librarian = Librarian.objects.create(name="Test Librarian", library=library)
        print(f"✓ Created librarian: {librarian.name}")
        
        print("\n🎉 All tests passed! relationship_app is working correctly.")
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        return False
    
    return True

if __name__ == "__main__":
    test_relationship_app()
