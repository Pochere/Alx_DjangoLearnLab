from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from .models import Book
from .serializers import BookSerializer

# Create your views here.
class BookListView(generics.ListAPIView):
    """
    GET /api/books/  -> returns JSON list of all books
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

  # Detail view (public)
class BookDetailView(generics.RetrieveAPIView):
    """
    GET /api/books/<id>/  -> returns details of one book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# Create view (auth required)
class BookCreateView(generics.CreateAPIView):
    """
    POST /api/books/create/  -> create a new book (auth required)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer  
    permission_classes = [permissions.IsAuthenticated]

# Update view (auth required)
class BookUpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH /api/books/<id>/update/  -> update a book (auth required)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

#  Delete view (auth required)
class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /api/books/<id>/delete/  -> delete a book (auth required)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

