from django.test import TestCase
from app.views import *
from app.models import Publisher, Author, Book

class TestURLS(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test_publisher = Publisher.objects.create(name='Test Publisher')
        cls.test_author = Author.objects.create(name='Test Author')
        cls.test_book = Book.objects.create(title='Test Book', publisher=cls.test_publisher)
        cls.test_book.authors.add(cls.test_author)

    def test_index_url(self):
        res = self.client.get('/')
        self.assertIs(res.status_code, 200)
    
    
    def test_book_create_get_url(self):
        res = self.client.get('/add-book/')
        self.assertIs(res.status_code, 200)
    

    def test_book_detail_url(self):
        res = self.client.get(f'/book/{self.test_book.pk}/')
        self.assertIs(res.status_code, 200)

    
    def test_book_delete_url(self):
        res = self.client.get(f'/delete-book/{self.test_book.pk}/')
        self.assertIs(res.status_code, 200)

