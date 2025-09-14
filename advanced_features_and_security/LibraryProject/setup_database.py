#!/usr/bin/env python
"""
Database setup script for the custom user model project.
This script helps set up the database with the custom user model.
"""

import os
import sys
import django
from datetime import date

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import CustomUser, UserProfile, Author, Book, Library, Librarian

def setup_database():
    """Set up the database with initial data."""
    print("Setting up database with custom user model...")
    
    # Create a superuser
    print("\n1. Creating superuser...")
    try:
        if not CustomUser.objects.filter(email='admin@library.com').exists():
            admin_user = CustomUser.objects.create_superuser(
                email='admin@library.com',
                username='admin',
                password='admin123',
                first_name='Library',
                last_name='Administrator',
                date_of_birth=date(1980, 1, 1)
            )
            print(f"✓ Created superuser: {admin_user.email}")
        else:
            print("✓ Superuser already exists")
    except Exception as e:
        print(f"✗ Error creating superuser: {e}")
    
    # Create sample authors
    print("\n2. Creating sample authors...")
    authors_data = [
        'J.K. Rowling',
        'George Orwell',
        'Harper Lee',
        'F. Scott Fitzgerald',
        'Jane Austen'
    ]
    
    for author_name in authors_data:
        try:
            author, created = Author.objects.get_or_create(name=author_name)
            if created:
                print(f"✓ Created author: {author.name}")
            else:
                print(f"✓ Author already exists: {author.name}")
        except Exception as e:
            print(f"✗ Error creating author {author_name}: {e}")
    
    # Create sample books
    print("\n3. Creating sample books...")
    books_data = [
        ('Harry Potter and the Philosopher\'s Stone', 'J.K. Rowling'),
        ('1984', 'George Orwell'),
        ('To Kill a Mockingbird', 'Harper Lee'),
        ('The Great Gatsby', 'F. Scott Fitzgerald'),
        ('Pride and Prejudice', 'Jane Austen'),
        ('Harry Potter and the Chamber of Secrets', 'J.K. Rowling'),
        ('Animal Farm', 'George Orwell'),
    ]
    
    for book_title, author_name in books_data:
        try:
            author = Author.objects.get(name=author_name)
            book, created = Book.objects.get_or_create(
                title=book_title,
                author=author
            )
            if created:
                print(f"✓ Created book: {book.title}")
            else:
                print(f"✓ Book already exists: {book.title}")
        except Exception as e:
            print(f"✗ Error creating book {book_title}: {e}")
    
    # Create sample libraries
    print("\n4. Creating sample libraries...")
    libraries_data = [
        'Central Library',
        'University Library',
        'Community Library',
        'Digital Library'
    ]
    
    for library_name in libraries_data:
        try:
            library, created = Library.objects.get_or_create(name=library_name)
            if created:
                print(f"✓ Created library: {library.name}")
            else:
                print(f"✓ Library already exists: {library.name}")
        except Exception as e:
            print(f"✗ Error creating library {library_name}: {e}")
    
    # Add books to libraries
    print("\n5. Adding books to libraries...")
    try:
        central_lib = Library.objects.get(name='Central Library')
        books = Book.objects.all()[:3]  # Add first 3 books
        for book in books:
            central_lib.books.add(book)
        print(f"✓ Added {books.count()} books to Central Library")
        
        university_lib = Library.objects.get(name='University Library')
        books = Book.objects.all()[3:6]  # Add next 3 books
        for book in books:
            university_lib.books.add(book)
        print(f"✓ Added {books.count()} books to University Library")
    except Exception as e:
        print(f"✗ Error adding books to libraries: {e}")
    
    # Create sample users with different roles
    print("\n6. Creating sample users...")
    users_data = [
        {
            'email': 'librarian@library.com',
            'username': 'librarian',
            'first_name': 'Sarah',
            'last_name': 'Johnson',
            'role': 'Librarian'
        },
        {
            'email': 'member@library.com',
            'username': 'member',
            'first_name': 'John',
            'last_name': 'Doe',
            'role': 'Member'
        }
    ]
    
    for user_data in users_data:
        try:
            if not CustomUser.objects.filter(email=user_data['email']).exists():
                user = CustomUser.objects.create_user(
                    email=user_data['email'],
                    username=user_data['username'],
                    first_name=user_data['first_name'],
                    last_name=user_data['last_name'],
                    password='password123',
                    date_of_birth=date(1990, 5, 15)
                )
                # Update the user's profile role
                if hasattr(user, 'profile'):
                    user.profile.role = user_data['role']
                    user.profile.save()
                print(f"✓ Created {user_data['role']}: {user.email}")
            else:
                print(f"✓ User already exists: {user_data['email']}")
        except Exception as e:
            print(f"✗ Error creating user {user_data['email']}: {e}")
    
    print("\n" + "="*50)
    print("Database setup completed!")
    print("="*50)
    print("\nYou can now:")
    print("1. Run the development server: python manage.py runserver")
    print("2. Access the admin interface at: http://127.0.0.1:8000/admin/")
    print("3. Login with: admin@library.com / admin123")
    print("4. Test the custom user model functionality")

if __name__ == '__main__':
    setup_database()
