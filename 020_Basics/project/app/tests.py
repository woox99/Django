from django.test import TestCase

class TestIndexView(TestCase):
    def test_index_URL(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_post(self):
        response = self.client.post('/', {
            'title': 'Test Title',
            'publisher': 'Test Publisher',
            'author': 'Test Author',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/confirmation/')


class TestConfirmationView(TestCase):
    def test_confirmation_URL(self):
        response = self.client.get('/confirmation/')
        self.assertEqual(response.status_code, 200)
