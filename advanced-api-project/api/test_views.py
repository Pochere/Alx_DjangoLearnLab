from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITestCase(TestCase):
    """
    Unit tests for Book API endpoints.
    A separate test database is automatically created and destroyed by Django,
    ensuring tests do not affect development or production data.
    """

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="tester", password="password123")

        # Create sample authors and books
        self.author = Author.objects.create(name="John Doe")
        self.book1 = Book.objects.create(
            title="Django for Beginners", author=self.author, publication_year=2021
        )
        self.book2 = Book.objects.create(
            title="Advanced Django", author=self.author, publication_year=2022
        )

    def test_list_books(self):
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Django for Beginners", str(response.data))

    def test_retrieve_book(self):
        response = self.client.get(f"/api/books/{self.book1.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Django for Beginners")

    def test_create_book_requires_authentication(self):
        data = {"title": "New Book", "author": self.author.id, "publication_year": 2023}
        response = self.client.post("/api/books/create/", data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Authenticated request
        self.client.login(username="tester", password="password123")
        response = self.client.post("/api/books/create/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Book")

    def test_update_book_requires_authentication(self):
        data = {"title": "Updated Title", "author": self.author.id, "publication_year": 2024}
        response = self.client.put(f"/api/books/{self.book1.id}/update/", data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Authenticated request
        self.client.login(username="tester", password="password123")
        response = self.client.put(f"/api/books/{self.book1.id}/update/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Title")

    def test_delete_book_requires_authentication(self):
        response = self.client.delete(f"/api/books/{self.book1.id}/delete/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Authenticated request
        self.client.login(username="tester", password="password123")
        response = self.client.delete(f"/api/books/{self.book1.id}/delete/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_search_books_by_title(self):
        response = self.client.get("/api/books/?search=Django")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)

    def test_filter_books_by_publication_year(self):
        response = self.client.get("/api/books/?publication_year=2021")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["publication_year"], 2021)

    def test_ordering_books_by_publication_year(self):
        response = self.client.get("/api/books/?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book["publication_year"] for book in response.data]
        self.assertEqual(years, sorted(years))
