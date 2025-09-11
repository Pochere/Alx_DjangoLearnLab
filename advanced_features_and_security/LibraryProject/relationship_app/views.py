from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404   
from .models import Library
from .models import Book
from .models import UserProfile
from .models import Author   


# Function-based view
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

# Registration view
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the new user automatically
            return redirect("list_books")  # Redirect after registration
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

class CustomLoginView(LoginView):
    template_name = "relationship_app/login.html"


class CustomLogoutView(LogoutView):
    template_name = "relationship_app/logged_out.html"
    

# Admin-only view
@user_passes_test(lambda u: u.is_authenticated and u.userprofile.role == 'Admin')
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")


# Librarian-only view
@user_passes_test(lambda u: u.is_authenticated and u.userprofile.role == 'Librarian')
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")


# Member-only view
@user_passes_test(lambda u: u.is_authenticated and u.userprofile.role == 'Member')
def member_view(request):
    return render(request, "relationship_app/member_view.html")

# View to add a book
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    # Example simple form handling
    if request.method == "POST":
        title = request.POST.get("title")
        author_id = request.POST.get("author")
        if title and author_id:
            Book.objects.create(title=title, author_id=author_id)
            return redirect("list_books")
    # You can use a template with a form to get title and author
    return render(request, "relationship_app/add_book.html", {"authors": Author.objects.all()})

# View to edit a book
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST.get("title")
        author_id = request.POST.get("author")
        if book.title and author_id:
            book.author_id = author_id
            book.save()
            return redirect("list_books")
    return render(request, "relationship_app/edit_book.html", {"book": book, "authors": Author.objects.all()})

# View to delete a book
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("list_books")
    return render(request, "relationship_app/delete_book.html", {"book": book})