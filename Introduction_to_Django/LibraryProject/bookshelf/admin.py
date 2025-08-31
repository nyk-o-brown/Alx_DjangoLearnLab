from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the Book model.
    
    This class provides a customized admin interface with:
    - List display fields for better visibility
    - Search capabilities
    - Filtering options
    - Read-only fields
    - Custom list display methods
    """
    
    # Fields to display in the list view
    list_display = ('title', 'author', 'publication_year', 'id', 'is_classic')
    
    # Fields that can be searched
    search_fields = ('title', 'author')
    
    # Fields to filter by in the right sidebar
    list_filter = ('publication_year', 'author')
    
    # Fields to display in the detail view (form)
    fields = ('title', 'author', 'publication_year')
    
    # Fields that are read-only (cannot be edited)
    readonly_fields = ('id',)
    
    # Number of items to display per page
    list_per_page = 20
    
    # Enable ordering by clicking on column headers
    ordering = ('title',)
    
    # Fields to display in the list view with custom formatting
    list_display_links = ('title', 'author')
    
    # Custom method to display publication year with century formatting
    def get_publication_year_display(self, obj):
        """Return publication year with century formatting."""
        if obj.publication_year:
            if obj.publication_year < 1900:
                return f"{obj.publication_year} (19th century)"
            elif obj.publication_year < 2000:
                return f"{obj.publication_year} (20th century)"
            else:
                return f"{obj.publication_year} (21st century)"
        return "Unknown"
    
    get_publication_year_display.short_description = "Publication Year (Century)"
    
    # Custom method to check if book is a classic (published before 1950)
    def is_classic(self, obj):
        """Return True if the book was published before 1950."""
        return obj.publication_year < 1950 if obj.publication_year else False
    
    is_classic.boolean = True
    is_classic.short_description = "Classic Book"
    
    # Customize the admin site header and title
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
