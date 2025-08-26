from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Add your custom fields to the admin forms:
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )

    list_display = ['username', 'email', 'first_name', 'last_name', 'date_of_birth', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)
