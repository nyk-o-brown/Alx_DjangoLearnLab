from django.db import models
from django.contrib.auth.models import Permission, User
from django.db.models.signals import post_save
from django.dispatch import receiver

# 🧑 Author Model: One author can write many books
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 📚 Book Model: Each book is written by one author
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    class Meta:
        Permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book")
            ("can_delete_book", "Can delete book")
        ]

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

# 👤 UserProfile Model: Extends User model with role-based access control
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')
    
    def __str__(self):
        return f"{self.user.username} - {self.role}"

# Signal to automatically create UserProfile when a User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()
    else:
        UserProfile.objects.create(user=instance)
