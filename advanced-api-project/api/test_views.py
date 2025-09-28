from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username="testuser", password="testpass")

        # Create authors
        self.author1 = Author.objects.create(name="Author One")
        self.author2 = Author.objects.create(name="Author Two")

        # Create books
        self.book1 = Book.objects.create(
            title="Django for Beginners",
            author=self.author1,
            publication_year=2020,
        )
        self.book2 = Book.objects.create(
            title="Advanced Django",
            author=self.author2,
            publication_year=2021,
        )

    def authenticate(self):
        """Helper method to login the test user."""
        self.client.login(username="testuser", password="testpass")

    def extract_items(self, response):
        """
        Handles both paginated and non-paginated responses.
        If response JSON has 'results', return that.
        Otherwise return the JSON list directly.
        """
        body = response.json()
        return body["results"] if isinstance(body, dict) and "results" in body else body

    # ---------------- Tests ----------------

    def test_list_books(self):
        url = reverse("book-list")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        items = self.extract_items(resp)
        self.assertEqual(len(items), 2)

    def test_retrieve_book(self):
        url = reverse("book-detail", args=[self.book1.id])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.json()["title"], "Django for Beginners")

    def test_create_book_requires_authentication(self):
        url = reverse("book-create")
        data = {
            "title": "New Book",
            "author": self.author1.id,
            "publication_year": 2022,
        }
        resp = self.client.post(url, data)
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)  # not logged in

        self.authenticate()
        resp = self.client.post(url, data)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test_update_book(self):
        url = reverse("book-update", args=[self.book1.id])
        data = {"title": "Updated Title", "author": self.author1.id, "publication_year": 2025}

        # Without login -> forbidden
        resp = self.client.put(url, data)
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)

        # With login
        self.authenticate()
        resp = self.client.put(url, data)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.json()["title"], "Updated Title")

    def test_delete_book(self):
        url = reverse("book-delete", args=[self.book1.id])

        # Without login
        resp = self.client.delete(url)
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)

        # With login
        self.authenticate()
        resp = self.client.delete(url)
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)

    def test_search_books_by_title(self):
        url = reverse("book-list") + "?search=django"
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        items = self.extract_items(resp)
        self.assertTrue(any("django" in b["title"].lower() for b in items))

    def test_filter_books_by_publication_year(self):
        url = reverse("book-list") + "?publication_year=2020"
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        items = self.extract_items(resp)
        self.assertTrue(all(b["publication_year"] == 2020 for b in items))

    def test_ordering_books_by_publication_year(self):
        url = reverse("book-list") + "?ordering=publication_year"
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        items = self.extract_items(resp)
        years = [b["publication_year"] for b in items]
        self.assertEqual(years, sorted(years))
