# Django Blog

A feature-rich blog application built with Django.

## Features

### Blog Post Management
- **View Posts**: All users can view the list of posts and individual post details
- **Create Posts**: Authenticated users can create new blog posts
- **Edit Posts**: Authors can edit their own posts
- **Delete Posts**: Authors can delete their own posts
- **Authentication**: User registration and login system
- **Permissions**: Role-based access control for post management

### Technical Features
- Class-based views for efficient code organization
- RESTful URL patterns
- Responsive templates with clean UI
- User authentication and authorization
- Pagination for post listings

## URL Patterns

- `GET /` - Home page with list of posts
- `GET /posts/` - All posts list
- `GET /posts/new/` - Create new post (requires login)
- `GET /posts/<id>/` - View specific post
- `GET /posts/<id>/edit/` - Edit post (requires login + ownership)
- `GET /posts/<id>/delete/` - Delete post (requires login + ownership)

## Authentication URLs

- `GET/POST /login/` - User login
- `GET/POST /logout/` - User logout
- `GET/POST /register/` - New user registration
- `GET/POST /profile/` - User profile

## Setup Instructions

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```

2. Install dependencies:
   ```bash
   pip install django
   ```

3. Run migrations:
   ```bash
   python manage.py migrate
   ```

4. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```

5. Run development server:
   ```bash
   python manage.py runserver
   ```

## Permissions

- Anonymous users can:
  - View post list and details
  - Register new account
  - Login to existing account

- Authenticated users can:
  - All anonymous user permissions
  - Create new posts
  - Edit their own posts
  - Delete their own posts
  - View and edit their profile

## Usage Examples

### Creating a Post
1. Login to your account
2. Click "Create New Post"
3. Fill in title and content
4. Click "Create Post"

### Editing a Post
1. Navigate to post detail
2. Click "Edit" (only visible if you're the author)
3. Modify content
4. Click "Update Post"

### Deleting a Post
1. Navigate to post detail
2. Click "Delete" (only visible if you're the author)
3. Confirm deletion
