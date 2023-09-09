from django.test import TestCase
from django.urls import reverse

# Create your tests here.

from .models import Book

class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="A good title",
            subtitle="An excellent subtitle",
            author="Tom Christie",
            isbn="1234567890123",
            price=25.00,
            description="A description",
        )
    
    def test_book_content(self):
        expected_title = self.book.title
        expected_subtitle = self.book.subtitle
        expected_author = self.book.author
        expected_isbn = self.book.isbn
        expected_price = self.book.price    
        expected_description = self.book.description
        self.assertEqual(expected_title, "A good title")
        self.assertEqual(expected_subtitle, "An excellent subtitle")
        self.assertEqual(expected_author, "Tom Christie")
        self.assertEqual(expected_isbn, "1234567890123")
        self.assertEqual(expected_price, 25.00)
        self.assertEqual(expected_description, "A description")


    def test_book_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A good title")
        # self.assertTemplateUsed(response, 'book_list.html')