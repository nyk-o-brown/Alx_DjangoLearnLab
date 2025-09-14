# Custom User Model Implementation

This project demonstrates the implementation of a custom user model in Django, extending Django's built-in authentication system with additional fields and functionality.

## Overview

The custom user model (`CustomUser`) extends Django's `AbstractUser` and includes:
- **date_of_birth**: A date field for storing user's birth date
- **profile_photo**: An image field for storing user's profile picture
- **Email-based authentication**: Uses email as the primary identifier instead of username

## Key Features

### 1. Custom User Model (`CustomUser`)
- Extends `AbstractUser` from Django's authentication system
- Adds `date_of_birth` and `profile_photo` fields
- Uses email as the unique identifier (`USERNAME_FIELD = 'email'`)
- Includes custom user manager for handling user creation

### 2. Custom User Manager (`CustomUserManager`)
- Handles user creation with email as the primary field
- Implements `create_user()` and `create_superuser()` methods
- Ensures proper validation and field handling

### 3. Admin Interface
- Custom admin configuration for managing users
- Displays profile photos in the admin interface
- Organized fieldsets for better user experience
- Enhanced search and filtering capabilities

### 4. Registration Form
- Custom registration form (`CustomUserCreationForm`)
- Includes all custom fields in the registration process
- Handles file uploads for profile photos

## File Structure

```
relationship_app/
├── models.py              # Custom user model and related models
├── admin.py               # Admin configuration
├── views.py               # Views with custom registration form
├── management/
│   └── commands/
│       └── create_custom_superuser.py  # Management command
└── templates/
    └── relationship_app/
        └── register.html  # Registration template (needs update)

LibraryProject/
├── settings.py            # Django settings with AUTH_USER_MODEL
└── urls.py               # URL configuration with media serving
```

## Configuration

### Settings Configuration
```python
# In settings.py
AUTH_USER_MODEL = 'relationship_app.CustomUser'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### URL Configuration
```python
# In urls.py
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## Usage

### 1. Creating Users Programmatically
```python
from relationship_app.models import CustomUser
from datetime import date

# Create a regular user
user = CustomUser.objects.create_user(
    email='user@example.com',
    username='username',
    first_name='John',
    last_name='Doe',
    date_of_birth=date(1990, 5, 15)
)

# Create a superuser
admin = CustomUser.objects.create_superuser(
    email='admin@example.com',
    username='admin',
    password='admin123',
    first_name='Admin',
    last_name='User'
)
```

### 2. Using the Management Command
```bash
python manage.py create_custom_superuser
```

### 3. Admin Interface
- Access the admin interface at `/admin/`
- Manage users with additional fields
- View profile photos in the user list
- Filter and search users by various fields

## Testing

Run the test script to verify the implementation:
```bash
python test_custom_user.py
```

## Migration Notes

⚠️ **Important**: This custom user model should be implemented before creating the first migration. If you have existing data, you'll need to:

1. Create a new database
2. Run migrations
3. Migrate data from the old user model if needed

## Key Benefits

1. **Flexibility**: Add any fields needed for your application
2. **Email Authentication**: Use email as the primary identifier
3. **Admin Integration**: Full admin support with custom fields
4. **Backward Compatibility**: Maintains Django's authentication features
5. **Extensibility**: Easy to add more fields in the future

## Related Models

The custom user model is integrated with:
- **UserProfile**: Role-based access control
- **All existing models**: Updated to reference the custom user model

## Security Considerations

- Profile photos are stored in a dedicated directory
- File uploads are handled securely
- User permissions and groups work as expected
- Password validation follows Django's standards

## Future Enhancements

Potential improvements:
- Add more user fields (phone, address, etc.)
- Implement user preferences
- Add user activity tracking
- Implement user verification system
- Add social authentication support
