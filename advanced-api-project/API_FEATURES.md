# API Filtering, Searching, and Ordering Guide

## Overview
This guide demonstrates how to use the filtering, searching, and ordering capabilities of the Book and Author APIs.

## Book API Features

### 1. Filtering
The Book API supports filtering by various fields:

#### Filter by Title
```
GET /api/books/?title=Python
```
Returns books with "Python" in the title (case-insensitive)

#### Filter by Publication Year Range
```
GET /api/books/?min_year=2020
GET /api/books/?max_year=2023
GET /api/books/?min_year=2020&max_year=2023
```
Returns books published within the specified year range

#### Filter by Author Name
```
GET /api/books/?author_name=John
```
Returns books whose author's name contains "John" (case-insensitive)

### 2. Searching
The search functionality looks across multiple fields:

```
GET /api/books/?search=python
```
Searches for "python" in both the book title and author name

### 3. Ordering
Results can be ordered by various fields:

#### Single Field Ordering
```
GET /api/books/?ordering=title
GET /api/books/?ordering=-title  # Descending order
GET /api/books/?ordering=publication_year
GET /api/books/?ordering=-publication_year
```

#### Multiple Field Ordering
```
GET /api/books/?ordering=author__name,title
GET /api/books/?ordering=-publication_year,title
```

## Author API Features

### 1. Searching
```
GET /api/authors/?search=john
```
Searches for authors with "john" in their name

### 2. Ordering
```
GET /api/authors/?ordering=name
GET /api/authors/?ordering=-name  # Descending order
```

## Combining Features
You can combine filtering, searching, and ordering in a single request:

```
GET /api/books/?search=python&min_year=2020&ordering=-publication_year
```
This would:
1. Search for "python" in titles and author names
2. Filter for books published from 2020 onwards
3. Order results by publication year (newest first)

## Pagination
Results are paginated with 10 items per page. Use the `page` parameter to navigate:

```
GET /api/books/?page=2
```

The response includes:
- `count`: Total number of items
- `next`: URL for the next page (null if none)
- `previous`: URL for the previous page (null if none)
- `results`: Current page's items

## Example Requests Using curl

1. Search for Python books published after 2020:
```bash
curl "http://localhost:8000/api/books/?search=python&min_year=2020"
```

2. Get newest books first:
```bash
curl "http://localhost:8000/api/books/?ordering=-publication_year"
```

3. Find all books by a specific author:
```bash
curl "http://localhost:8000/api/books/?author_name=Martin"
```

4. Complex query combining multiple features:
```bash
curl "http://localhost:8000/api/books/?search=python&min_year=2020&ordering=-publication_year&author_name=John"
```