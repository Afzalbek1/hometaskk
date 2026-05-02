from django.test import TestCase
from .models import Category, Book

class BookModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name="Test Category",
            description="Test desc"
        )

        self.book = Book.objects.create(
            category=self.category,
            title="Test Book",
            author="Test Author",
            description="Test desc",
            price=100,
            is_active=True
        )

    def test_all_books(self):
        books = Book.objects.all()
        self.assertEqual(books.count(), 1)

    def test_single_book(self):
        book = Book.objects.get(id=self.book.id)
        self.assertEqual(book.title, "Test Book")
        self.assertEqual(book.author, "Test Author")