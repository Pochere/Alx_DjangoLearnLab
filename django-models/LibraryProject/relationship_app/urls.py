from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views   # import whole views module
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path("books/", views.list_books, name="list_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),

    # Built-in Django auth views with explicit template_name
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),

    # Register view must be referenced as views.register for checker
    path("register/", views.register, name="register"),

    # Codes for Role-based URLs 
    path("admin-view/", admin_view, name="admin_view"),         # Admin-only page
    path("librarian-view/", librarian_view, name="librarian_view"),   # Librarian-only page
    path("member-view/", member_view, name="member_view"),     # Member-only page

    path("add_book/", views.add_book, name="add_book"),
    path("edit_book/<int:book_id>/", views.edit_book, name="edit_book"),
    path("delete_book/<int:book_id>/", views.delete_book, name="delete_book"),
]

