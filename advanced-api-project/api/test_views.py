from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Book
from django.contrib.auth.models import User


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a user for authenticated endpoints
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client.login(username="testuser", password="password123")

        # Create authors
        self.author1 = Author.objects.create(name="J.K. Rowling")
        self.author2 = Author.objects.create(name="George Orwell")

        # Create books
        self.book1 = Book.objects.create(
            title="Harry Potter", publication_year=1997, author=self.author1
        )
        self.book2 = Book.objects.create(
            title="1984", publication_year=1949, author=self.author2
        )

    # -----------------------------
    # CRUD Tests
    # -----------------------------
    def test_list_books(self):
        url = reverse("book-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book(self):
        url = reverse("book-detail", args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)

    def test_create_book_authenticated(self):
        url = reverse("book-create")
        data = {"title": "New Book", "publication_year": 2020, "author": self.author1.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book_authenticated(self):
        url = reverse("book-update", args=[self.book1.id])
        data = {"title": "Updated Title", "publication_year": 1997, "author": self.author1.id}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book_authenticated(self):
        url = reverse("book-delete", args=[self.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # -----------------------------
    # Permission Tests
    # -----------------------------
    def test_create_book_unauthenticated(self):
        self.client.logout()
        url = reverse("book-create")
        data = {"title": "Unauthorized Book", "publication_year": 2022, "author": self.author1.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # -----------------------------
    # Filtering, Searching, Ordering Tests
    # -----------------------------
    def test_filter_by_title(self):
        url = reverse("book-list") + "?title=1984"
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "1984")

    def test_search_by_author_name(self):
        url = reverse("book-list") + "?search=Rowling"
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["author"], self.author1.id)

    def test_order_by_publication_year_desc(self):
        url = reverse("book-list") + "?ordering=-publication_year"
        response = self.client.get(url)
        self.assertEqual(response.data[0]["title"], "Harry Potter")
