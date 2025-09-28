# API Testing Documentation

## Overview
This document outlines the testing strategy and guidelines for the Advanced API Project. The test suite covers CRUD operations, filtering, searching, ordering, and authentication/permissions for both Book and Author models.

## Test Structure

### Base Test Class (`APIBaseTestCase`)
- Sets up test data including users, authors, and books
- Provides authentication helpers
- Configures API client and common URLs

### Test Categories

1. **Book CRUD Tests** (`BookCRUDTests`)
   - Create book (authenticated/unauthenticated)
   - Retrieve book list and details
   - Update book details
   - Delete book

2. **Book Filter & Search Tests** (`BookFilterSearchTests`)
   - Filter by title
   - Filter by publication year range
   - Search functionality
   - Ordering options

3. **Author Tests** (`AuthorTests`)
   - Create author
   - Retrieve author list
   - Search authors

## Running the Tests

### Basic Test Execution
```bash
python manage.py test api
```

### Running Specific Test Cases
```bash
# Run all book tests
python manage.py test api.test_views.BookCRUDTests

# Run specific test method
python manage.py test api.test_views.BookCRUDTests.test_create_book
```

### Test with Coverage Report
```bash
coverage run --source='.' manage.py test api
coverage report
```

## Test Data

### Pre-configured Test Data
- **Users**: testuser (password: testpass123)
- **Authors**: John Smith, Jane Doe
- **Books**: 
  - Python Testing (2023)
  - Django REST APIs (2022)
  - JavaScript Basics (2021)

## Authentication in Tests

### How to Authenticate
```python
# In test methods
self.authenticate()  # Authenticates as testuser
```

## Testing Strategy

### CRUD Operations
- Verify correct status codes
- Validate response data
- Check database state changes
- Test both authenticated and unauthenticated access

### Filtering & Searching
- Test exact matches
- Test partial matches
- Verify case insensitivity
- Check multiple filter combinations

### Ordering
- Test ascending and descending orders
- Verify multiple field ordering
- Check default ordering

### Permissions
- Verify unauthenticated access restrictions
- Confirm authenticated access permissions
- Test different HTTP methods

## Common Test Assertions

### Status Code Checks
```python
self.assertEqual(response.status_code, status.HTTP_200_OK)
self.assertEqual(response.status_code, status.HTTP_201_CREATED)
self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
```

### Data Validation
```python
self.assertEqual(response.data['title'], 'Expected Title')
self.assertEqual(len(response.data['results']), expected_count)
```

### Database State
```python
self.assertEqual(Book.objects.count(), expected_count)
self.assertTrue(Book.objects.filter(title='New Book').exists())
```

## Test Coverage Goals

1. **Model Coverage**
   - All model fields validated
   - Model methods tested
   - Field constraints verified

2. **View Coverage**
   - All endpoints tested
   - All HTTP methods verified
   - Error cases handled

3. **Authentication Coverage**
   - Permission classes tested
   - Authentication requirements verified
   - Unauthenticated access checked

## Adding New Tests

When adding new features:
1. Create new test class or add methods to existing classes
2. Follow naming convention: `test_<feature_name>`
3. Include both positive and negative test cases
4. Document test purpose in method docstring

## Interpreting Test Results

### Success Output
```
Creating test database...
..........................
----------------------------------------------------------------------
Ran 26 tests in 2.345s

OK
Destroying test database...
```

### Common Issues
- Database errors: Check test database configuration
- Authentication errors: Verify test user setup
- Data validation errors: Check test data setup

## Maintenance

### Regular Tasks
1. Run full test suite before deployments
2. Update tests when adding new features
3. Maintain test data relevance
4. Review test coverage reports

### Best Practices
1. Keep tests focused and atomic
2. Use clear, descriptive test names
3. Maintain test documentation
4. Regular test maintenance with code changes