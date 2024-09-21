from django.test import TestCase
from app.models import Publisher, Author, Book

class TestModels(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test_publisher = Publisher.objects.create(name='Test Publisher')
        cls.test_author = Author.objects.create(name='Test Author')
        cls.test_book = Book.objects.create(title='Test Book', publisher=cls.test_publisher)
        cls.test_book.authors.add(cls.test_author)

    
    def test_publisher_model(self):
        self.assertEqual(str(self.test_publisher), 'Test Publisher')

    
    def test_author_model(self):
        self.assertEqual(str(self.test_author), 'Test Author')


    def test_book_model(self):
        self.assertEqual(str(self.test_book), 'Test Book')
        self.assertEqual(self.test_book.publisher, self.test_publisher)
        self.assertIn(self.test_author, self.test_book.authors.all())