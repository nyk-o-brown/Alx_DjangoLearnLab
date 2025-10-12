# Social Media API - Follow System and Feed

## Follow System

### Follow a User
```
POST /api/accounts/follow/{user_id}/
```
Follow another user. Requires authentication.

Response:
- 200: Successfully followed user
- 400: Cannot follow yourself
- 404: User not found

### Unfollow a User
```
POST /api/accounts/unfollow/{user_id}/
```
Unfollow a user you're currently following. Requires authentication.

Response:
- 200: Successfully unfollowed user
- 404: User not found

### User Profile
```
GET /api/accounts/profile/
```
Get your own profile information including:
- Basic user details
- Follower count
- Following count

Example response:
```json
{
    "id": 1,
    "username": "user1",
    "email": "user1@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "bio": "My bio",
    "profile_picture": "http://example.com/media/profile_pics/1.jpg",
    "follower_count": 10,
    "following_count": 15,
    "date_joined": "2025-10-12T10:00:00Z",
    "updated_at": "2025-10-12T10:00:00Z"
}
```

## Feed System

### Get Personal Feed
```
GET /api/posts/feed/
```
Get a personalized feed of posts from users you follow. Posts are ordered by creation date (newest first).

Features:
- Pagination (10 items per page)
- Only shows posts from followed users
- Includes post author details

Example response:
```json
{
    "count": 25,
    "next": "http://example.com/api/posts/feed/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "author": {
                "id": 2,
                "username": "user2",
                "profile_picture": "http://example.com/media/profile_pics/2.jpg"
            },
            "title": "Latest Post",
            "content": "Post content here",
            "created_at": "2025-10-12T11:00:00Z",
            "updated_at": "2025-10-12T11:00:00Z",
            "comment_count": 5
        },
        // ... more posts
    ]
}
```

## Example Usage

### Following a User
```bash
curl -X POST http://localhost:8000/api/accounts/follow/2/ \
  -H "Authorization: Token <your_token>"
```

### Getting Your Feed
```bash
curl http://localhost:8000/api/posts/feed/ \
  -H "Authorization: Token <your_token>"
```

### Getting Your Profile
```bash
curl http://localhost:8000/api/accounts/profile/ \
  -H "Authorization: Token <your_token>"
```