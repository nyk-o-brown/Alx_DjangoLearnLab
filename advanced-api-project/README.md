# Advanced API Project

This project demonstrates the implementation of a RESTful API using Django REST Framework with advanced features including custom serializers, generic views, filtering, and authentication.

## Features

- CRUD operations for Books and Authors
- Nested serializers for related data
- Permission-based access control
- Advanced filtering capabilities
- Pagination support
- Authentication using Session and Basic authentication

## API Endpoints

### Books

- `GET /api/books/`: List all books (public access)
- `POST /api/books/`: Create a new book (authenticated users only)
- `GET /api/books/{id}/`: Retrieve a specific book (public access)
- `PUT /api/books/{id}/`: Update a book (authenticated users only)
- `DELETE /api/books/{id}/`: Delete a book (authenticated users only)

Filtering options for /api/books/:
- `title`: Filter by book title (case-insensitive contains)
- `min_year`: Filter by minimum publication year
- `max_year`: Filter by maximum publication year
- `author_name`: Filter by author name (case-insensitive contains)

### Authors

- `GET /api/authors/`: List all authors (public access)
- `POST /api/authors/`: Create a new author (authenticated users only)
- `GET /api/authors/{id}/`: Retrieve a specific author (public access)
- `PUT /api/authors/{id}/`: Update an author (authenticated users only)
- `DELETE /api/authors/{id}/`: Delete an author (authenticated users only)

## Authentication

The API uses Django REST Framework's built-in authentication classes:
- Session Authentication
- Basic Authentication

To authenticate:
1. Access the browsable API at `/api/`
2. Use the login link at the top right
3. Log in with your credentials

For programmatic access, use Basic Authentication by including an `Authorization` header:
```
Authorization: Basic <base64-encoded-credentials>
```

## Permissions

- Anonymous users can read all endpoints (GET requests)
- Authenticated users can perform all operations (GET, POST, PUT, DELETE)
- Custom permissions can be added per view as needed

## Pagination

Results are paginated with 10 items per page. Response format:
```json
{
    "count": total_items,
    "next": next_page_url,
    "previous": previous_page_url,
    "results": [
        // items
    ]
}
```

## Testing the API

You can test the API using:
1. The browsable API interface at `/api/`
2. Command line tools like `curl`
3. API testing tools like Postman

Example curl commands:

List all books:
```bash
curl http://localhost:8000/api/books/
```

Create a new book (authenticated):
```bash
curl -X POST http://localhost:8000/api/books/ \
    -H "Content-Type: application/json" \
    -u "username:password" \
    -d '{"title":"New Book","publication_year":2023,"author":1}'
```

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install django djangorestframework django-filter
   ```
3. Apply migrations:
   ```bash
   python manage.py migrate
   ```
4. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Future Improvements

- Add JWT authentication
- Implement rate limiting
- Add caching
- Create more detailed filtering options
- Add API versioning