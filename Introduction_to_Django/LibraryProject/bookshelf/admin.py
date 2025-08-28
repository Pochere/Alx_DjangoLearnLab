from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book

# Customize the admin interface for Book
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  # show these columns in the list
    list_filter = ("publication_year", "author")            # add filters in sidebar
    search_fields = ("title", "author")                     # enable search box for title & author

# Register the model with its custom admin class
admin.site.register(Book, BookAdmin)
