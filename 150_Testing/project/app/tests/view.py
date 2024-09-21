from django.test import TestCase
from app.models import Publisher, Author, Book

class TestViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test_publisher = Publisher.objects.create(name='Test Publisher')
        cls.test_author = Author.objects.create(name='Test Author')


    def test_book_create_post(self):
        book_data = {
            'title' : 'book_create Test Book',
            'publisher' : self.test_publisher.pk,
            'authors' : [self.test_author.pk]
        }
        res = self.client.post('/add-book/', data=book_data)
        self.assertEqual(res.status_code, 302) # 302 is successfully redirected status code
        self.assertTrue(Book.objects.filter(title='book_create Test Book').exists()) # check if the book exists
        test_book = Book.objects.get(title='book_create Test Book')
        self.assertEqual(test_book.publisher.pk, self.test_publisher.pk) # check if publisher was created
        self.assertIn(self.test_author, test_book.authors.all()) # check if author was added


    def test_book_delete_post(self):
        test_book = Book.objects.create(title='book-delete Test Book', publisher=self.test_publisher)
        test_book.authors.add(self.test_author)
        res = self.client.post(f'/delete-book/{test_book.pk}/')
        self.assertEqual(res.status_code, 302) # 302 is successfully redirected status code
        self.assertFalse(Book.objects.filter(title='book_delete Test Book').exists()) # check if the book exists


