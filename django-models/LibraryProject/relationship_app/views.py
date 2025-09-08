from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test   # ✅ NEW
from .models import Library
from .models import Book
from .models import UserProfile

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
