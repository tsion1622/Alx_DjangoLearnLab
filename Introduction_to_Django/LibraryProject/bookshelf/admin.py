from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Show in list view
    search_fields = ('title', 'author')                    # Enable search
    list_filter = ('publication_year',)                    # Enable filtering
