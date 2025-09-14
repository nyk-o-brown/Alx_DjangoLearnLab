#!/usr/bin/env python
"""
Test script to demonstrate the custom user model functionality.
Run this script to test the custom user model implementation.
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

def test_custom_user_creation():
    """Test creating users with the custom user model."""
    print("=== Testing Custom User Model ===")
    
    # Test 1: Create a regular user
    print("\n1. Creating a regular user...")
    try:
        user1 = CustomUser.objects.create_user(
            email='john.doe@example.com',
            username='johndoe',
            first_name='John',
            last_name='Doe',
            date_of_birth=date(1990, 5, 15)
        )
        print(f"✓ Created user: {user1}")
        print(f"  - Email: {user1.email}")
        print(f"  - Full name: {user1.get_full_name()}")
        print(f"  - Date of birth: {user1.date_of_birth}")
        print(f"  - Profile created: {hasattr(user1, 'profile')}")
        if hasattr(user1, 'profile'):
            print(f"  - Role: {user1.profile.role}")
    except Exception as e:
        print(f"✗ Error creating user: {e}")
    
    # Test 2: Create a superuser
    print("\n2. Creating a superuser...")
    try:
        superuser = CustomUser.objects.create_superuser(
            email='admin@example.com',
            username='admin',
            password='admin123',
            first_name='Admin',
            last_name='User',
            date_of_birth=date(1985, 1, 1)
        )
        print(f"✓ Created superuser: {superuser}")
        print(f"  - Is staff: {superuser.is_staff}")
        print(f"  - Is superuser: {superuser.is_superuser}")
    except Exception as e:
        print(f"✗ Error creating superuser: {e}")
    
    # Test 3: Test user authentication
    print("\n3. Testing user authentication...")
    try:
        # Test email-based authentication
        user = CustomUser.objects.get(email='john.doe@example.com')
        print(f"✓ Found user by email: {user}")
        
        # Test username-based authentication
        user = CustomUser.objects.get(username='johndoe')
        print(f"✓ Found user by username: {user}")
    except Exception as e:
        print(f"✗ Error in authentication test: {e}")

def test_related_models():
    """Test the related models with custom user."""
    print("\n=== Testing Related Models ===")
    
    try:
        # Create some test data
        author = Author.objects.create(name='Test Author')
        book = Book.objects.create(title='Test Book', author=author)
        library = Library.objects.create(name='Test Library')
        library.books.add(book)
        librarian = Librarian.objects.create(name='Test Librarian', library=library)
        
        print("✓ Created test data:")
        print(f"  - Author: {author}")
        print(f"  - Book: {book}")
        print(f"  - Library: {library}")
        print(f"  - Librarian: {librarian}")
        
        # Test user profile
        user = CustomUser.objects.filter(email='john.doe@example.com').first()
        if user and hasattr(user, 'profile'):
            user.profile.role = 'Librarian'
            user.profile.save()
            print(f"✓ Updated user role: {user.profile.role}")
        
    except Exception as e:
        print(f"✗ Error in related models test: {e}")

def cleanup_test_data():
    """Clean up test data."""
    print("\n=== Cleaning up test data ===")
    try:
        CustomUser.objects.filter(email__in=['john.doe@example.com', 'admin@example.com']).delete()
        Author.objects.filter(name='Test Author').delete()
        Book.objects.filter(title='Test Book').delete()
        Library.objects.filter(name='Test Library').delete()
        Librarian.objects.filter(name='Test Librarian').delete()
        print("✓ Cleaned up test data")
    except Exception as e:
        print(f"✗ Error cleaning up: {e}")

if __name__ == '__main__':
    print("Custom User Model Test Script")
    print("=" * 40)
    
    test_custom_user_creation()
    test_related_models()
    
    # Ask if user wants to clean up
    cleanup = input("\nDo you want to clean up test data? (y/n): ").lower().strip()
    if cleanup == 'y':
        cleanup_test_data()
    
    print("\nTest completed!")
