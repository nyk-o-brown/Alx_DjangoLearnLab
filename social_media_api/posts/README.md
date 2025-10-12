# Social Media API - Posts and Comments

This documentation covers the posts and comments endpoints of the Social Media API.

## Base URL
All endpoints are prefixed with `/api/posts/`

## Authentication
All write operations require authentication using Token Authentication. Include the token in the Authorization header:
```
Authorization: Token <your_token_here>
```

## Endpoints

### Posts

#### List Posts
```
GET /api/posts/
```
- Supports pagination (10 items per page)
- Filtering options:
  - `title`: Filter by title (case-insensitive) - `/api/posts/?title=search_term`
  - `content`: Filter by content (case-insensitive) - `/api/posts/?content=search_term`
- Response includes author details, creation date, and comment count

#### Create Post
```
POST /api/posts/
```
Required fields:
- `title`: String (max 200 characters)
- `content`: String

#### Get Single Post
```
GET /api/posts/{post_id}/
```
Returns detailed post information including comments

#### Update Post
```
PUT /api/posts/{post_id}/
PATCH /api/posts/{post_id}/
```
- Only the author can update their posts
- Supports partial updates via PATCH

#### Delete Post
```
DELETE /api/posts/{post_id}/
```
Only the author can delete their posts

### Comments

#### List Post Comments
```
GET /api/posts/{post_id}/comments/
```
- Supports pagination (10 items per page)
- Returns comments for a specific post

#### Create Comment
```
POST /api/posts/{post_id}/comments/
```
Required fields:
- `content`: String

#### Update Comment
```
PUT /api/posts/{post_id}/comments/{comment_id}/
PATCH /api/posts/{post_id}/comments/{comment_id}/
```
- Only the author can update their comments
- Supports partial updates via PATCH

#### Delete Comment
```
DELETE /api/posts/{post_id}/comments/{comment_id}/
```
Only the author can delete their comments

## Example Requests

### Creating a Post
```bash
curl -X POST http://localhost:8000/api/posts/ \
  -H "Authorization: Token <your_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My First Post",
    "content": "This is the content of my post."
  }'
```

### Adding a Comment
```bash
curl -X POST http://localhost:8000/api/posts/1/comments/ \
  -H "Authorization: Token <your_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "content": "This is a comment on the post."
  }'
```

### Filtering Posts
```bash
# Search posts by title
curl http://localhost:8000/api/posts/?title=search_term

# Search posts by content
curl http://localhost:8000/api/posts/?content=search_term
```

## Error Responses

The API uses standard HTTP status codes:
- 200: Success
- 201: Created
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 500: Internal Server Error

Error responses include a message explaining the error:
```json
{
    "detail": "Error message here"
}
```