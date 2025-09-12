# LibraryProject

This is my first Django project for ALX.  
Steps completed: Installed Django, created project, and ran the development server.


Django Admin Integration – Book Model
Steps Followed
1. Created a Django Project and App

Started a new Django project called LibraryProject.

Created an app (e.g., bookshelf) to manage the Book model.

2. Defined the Book Model

In bookshelf/models.py, created a Book model with fields:

title (CharField)

author (CharField)

publication_year (IntegerField)

3. Registered the Book Model in Admin

In bookshelf/admin.py, customized the admin interface:

from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  # show these columns
    list_filter = ("publication_year", "author")            # filters in sidebar
    search_fields = ("title", "author")                     # search functionality

admin.site.register(Book, BookAdmin)

4. Ran Migrations

Applied migrations so the database could store Book records:

python manage.py makemigrations
python manage.py migrate

5. Created a Superuser

Created an admin user to access the Django Admin site:

python manage.py createsuperuser


Entered username, email, and password.

Logged in at: http://127.0.0.1:8000/admin/
.

6. Tested the Admin Interface

Confirmed that Books appeared in the admin sidebar.

Added a new Book entry.

Verified that:

The list view showed title, author, publication year.

Filters for author and publication_year were available.

Search functionality worked for title and author.

✅ Result: The Book model is fully integrated into the Django Admin with custom list display, filtering, and search functionality.

# LibraryProject - Permissions and Groups

This project demonstrates how to use **custom permissions** and **groups** in Django.

## Permissions
We defined custom permissions in `Book` model (`bookshelf/models.py`):
- **can_create** → Allows creating new books.
- **can_edit** → Allows editing existing books.

## Views
We applied permission checks in `bookshelf/views.py` using `@permission_required`:
- `add_book` view requires `can_create`
- `edit_book` view requires `can_edit`

## Groups
Admins can assign users to groups and grant these permissions via the Django admin panel:
1. Go to **Admin → Groups**.
2. Create groups like **Librarian** or **Member**.
3. Assign permissions (`can_create`, `can_edit`) to these groups.
4. Add users to groups.


