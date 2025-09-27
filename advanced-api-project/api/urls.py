from django.urls import path
from .views import BookListView
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),     # POST create
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),   # GET detail
    path('books/update/', BookUpdateView.as_view(), name='book-update'), # PUT/PATCH
    path('books/delete/', BookDeleteView.as_view(), name='book-delete'), # DELETE
]
