#!/usr/bin/env python
"""
Demonstration script for the custom user model.
This script shows various ways to interact with the custom user model.
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

from relationship_app.models import CustomUser, UserProfile, Author, Book, Library

def demonstrate_user_creation():
    """Demonstrate different ways to create users."""
    print("=== User Creation Examples ===")
    
    # Example 1: Create user with minimal data
    print("\n1. Creating user with minimal data:")
    try:
        user1 = CustomUser.objects.create_user(
            email='minimal@example.com',
            username='minimal_user',
            password='password123'
        )
        print(f"✓ Created: {user1}")
        print(f"  - Email: {user1.email}")
        print(f"  - Username: {user1.username}")
        print(f"  - Full name: {user1.get_full_name()}")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # Example 2: Create user with all custom fields
    print("\n2. Creating user with all custom fields:")
    try:
        user2 = CustomUser.objects.create_user(
            email='complete@example.com',
            username='complete_user',
            password='password123',
            first_name='Complete',
            last_name='User',
            date_of_birth=date(1995, 8, 20)
        )
        print(f"✓ Created: {user2}")
        print(f"  - Email: {user2.email}")
        print(f"  - Full name: {user2.get_full_name()}")
        print(f"  - Date of birth: {user2.date_of_birth}")
        print(f"  - Profile photo: {user2.profile_photo}")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # Example 3: Create superuser
    print("\n3. Creating superuser:")
    try:
        superuser = CustomUser.objects.create_superuser(
            email='super@example.com',
            username='super_user',
            password='password123',
            first_name='Super',
            last_name='User',
            date_of_birth=date(1985, 3, 10)
        )
        print(f"✓ Created superuser: {superuser}")
        print(f"  - Is staff: {superuser.is_staff}")
        print(f"  - Is superuser: {superuser.is_superuser}")
    except Exception as e:
        print(f"✗ Error: {e}")

def demonstrate_user_queries():
    """Demonstrate different ways to query users."""
    print("\n=== User Query Examples ===")
    
    # Query by email
    print("\n1. Query by email:")
    try:
        user = CustomUser.objects.get(email='complete@example.com')
        print(f"✓ Found user by email: {user}")
    except CustomUser.DoesNotExist:
        print("✗ User not found")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # Query by username
    print("\n2. Query by username:")
    try:
        user = CustomUser.objects.get(username='complete_user')
        print(f"✓ Found user by username: {user}")
    except CustomUser.DoesNotExist:
        print("✗ User not found")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # Filter users by date of birth
    print("\n3. Filter users by date of birth:")
    try:
        users = CustomUser.objects.filter(date_of_birth__year=1995)
        print(f"✓ Found {users.count()} users born in 1995:")
        for user in users:
            print(f"  - {user.email} ({user.date_of_birth})")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # Filter users by first name
    print("\n4. Filter users by first name:")
    try:
        users = CustomUser.objects.filter(first_name__icontains='Complete')
        print(f"✓ Found {users.count()} users with 'Complete' in first name:")
        for user in users:
            print(f"  - {user.email} ({user.get_full_name()})")
    except Exception as e:
        print(f"✗ Error: {e}")

def demonstrate_user_profile():
    """Demonstrate user profile functionality."""
    print("\n=== User Profile Examples ===")
    
    # Get user and their profile
    print("\n1. Accessing user profile:")
    try:
        user = CustomUser.objects.get(email='complete@example.com')
        if hasattr(user, 'profile'):
            profile = user.profile
            print(f"✓ User: {user.email}")
            print(f"  - Role: {profile.role}")
            print(f"  - Profile ID: {profile.id}")
        else:
            print("✗ No profile found for user")
    except CustomUser.DoesNotExist:
        print("✗ User not found")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # Update user profile
    print("\n2. Updating user profile:")
    try:
        user = CustomUser.objects.get(email='complete@example.com')
        if hasattr(user, 'profile'):
            profile = user.profile
            profile.role = 'Librarian'
            profile.save()
            print(f"✓ Updated role to: {profile.role}")
        else:
            print("✗ No profile found for user")
    except CustomUser.DoesNotExist:
        print("✗ User not found")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # Filter users by role
    print("\n3. Filter users by role:")
    try:
        librarian_profiles = UserProfile.objects.filter(role='Librarian')
        print(f"✓ Found {librarian_profiles.count()} librarians:")
        for profile in librarian_profiles:
            print(f"  - {profile.user.email} ({profile.role})")
    except Exception as e:
        print(f"✗ Error: {e}")

def demonstrate_authentication():
    """Demonstrate authentication with custom user model."""
    print("\n=== Authentication Examples ===")
    
    from django.contrib.auth import authenticate
    
    # Authenticate with email
    print("\n1. Authenticate with email:")
    try:
        user = authenticate(email='complete@example.com', password='password123')
        if user:
            print(f"✓ Authentication successful: {user}")
            print(f"  - Is authenticated: {user.is_authenticated}")
            print(f"  - Is active: {user.is_active}")
        else:
            print("✗ Authentication failed")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # Authenticate with username
    print("\n2. Authenticate with username:")
    try:
        user = authenticate(username='complete_user', password='password123')
        if user:
            print(f"✓ Authentication successful: {user}")
        else:
            print("✗ Authentication failed")
    except Exception as e:
        print(f"✗ Error: {e}")

def cleanup_demo_data():
    """Clean up demo data."""
    print("\n=== Cleaning up demo data ===")
    try:
        CustomUser.objects.filter(
            email__in=['minimal@example.com', 'complete@example.com', 'super@example.com']
        ).delete()
        print("✓ Cleaned up demo users")
    except Exception as e:
        print(f"✗ Error cleaning up: {e}")

if __name__ == '__main__':
    print("Custom User Model Demonstration")
    print("=" * 40)
    
    demonstrate_user_creation()
    demonstrate_user_queries()
    demonstrate_user_profile()
    demonstrate_authentication()
    
    # Ask if user wants to clean up
    cleanup = input("\nDo you want to clean up demo data? (y/n): ").lower().strip()
    if cleanup == 'y':
        cleanup_demo_data()
    
    print("\nDemonstration completed!")
