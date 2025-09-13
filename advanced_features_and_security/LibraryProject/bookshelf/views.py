from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm

# View books (only for users with can_view permission)
@permission_required('bookshelf.can_view', raise_exception=True)
def list_books(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/list_books.html', {'books': books})

# Add a new book (only for users with can_create permission)
@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    return render(request, 'bookshelf/add_book.html')

# Edit book (only for users with can_edit permission)
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    return render(request, 'bookshelf/edit_book.html', {'book_id': book_id})

# Delete book (only for users with can_delete permission)
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    return render(request, 'bookshelf/delete_book.html', {'book_id': book_id})

# View book (only for users with can_view permission)
@permission_required("bookshelf.view_book", raise_exception=True)
def book_list(request):
    """Display a list of all books (requires view_book permission)."""
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

# NEW CODE ADDED BELOW

def form_example(request):
    """A simple view to demonstrate ExampleForm usage."""
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            # For now, just render the same form with a success message
            return render(request, "bookshelf/form_example.html", {
                "form": form,
                "message": "Form submitted successfully!"
            })
    else:
        form = ExampleForm()

    return render(request, "bookshelf/form_example.html", {"form": form})
