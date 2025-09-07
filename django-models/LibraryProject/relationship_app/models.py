from django.db import models

# 🧑 Author Model: One author can write many books
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 📚 Book Model: Each book is written by one author
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} by {self.author.name}"

# 🏛️ Library Model: A library can hold many books
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name

# 👩‍💼 Librarian Model: Each library has one librarian
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')

    def __str__(self):
        return f"{self.name} (Librarian of {self.library.name})"
