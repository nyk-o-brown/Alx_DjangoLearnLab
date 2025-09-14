from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import CustomUser, UserProfile, Author, Book, Library, Librarian

# Custom User Admin
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """
    Custom admin configuration for the CustomUser model.
    """
    list_display = ('email', 'username', 'first_name', 'last_name', 'date_of_birth', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'date_joined', 'date_of_birth')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('email',)
    
    # Fields to display in the user detail form
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username', 'first_name', 'last_name', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    # Fields to display when adding a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'last_name', 'password1', 'password2', 'date_of_birth', 'profile_photo'),
        }),
    )
    
    # Custom method to display profile photo in admin
    def get_profile_photo(self, obj):
        if obj.profile_photo:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%;" />', obj.profile_photo.url)
        return "No photo"
    get_profile_photo.short_description = 'Profile Photo'

# UserProfile Admin
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin configuration for UserProfile model.
    """
    list_display = ('user', 'role', 'get_user_email', 'get_user_name')
    list_filter = ('role',)
    search_fields = ('user__email', 'user__username', 'user__first_name', 'user__last_name')
    
    def get_user_email(self, obj):
        return obj.user.email
    get_user_email.short_description = 'Email'
    
    def get_user_name(self, obj):
        return obj.user.get_full_name()
    get_user_name.short_description = 'Full Name'

# Author Admin
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'book_count')
    search_fields = ('name',)
    
    def book_count(self, obj):
        return obj.books.count()
    book_count.short_description = 'Number of Books'

# Book Admin
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'library_count')
    list_filter = ('author',)
    search_fields = ('title', 'author__name')
    
    def library_count(self, obj):
        return obj.libraries.count()
    library_count.short_description = 'Number of Libraries'

# Library Admin
@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name', 'book_count', 'has_librarian')
    search_fields = ('name',)
    
    def book_count(self, obj):
        return obj.books.count()
    book_count.short_description = 'Number of Books'
    
    def has_librarian(self, obj):
        return bool(obj.librarian)
    has_librarian.boolean = True
    has_librarian.short_description = 'Has Librarian'

# Librarian Admin
@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('name', 'library')
    search_fields = ('name', 'library__name')
