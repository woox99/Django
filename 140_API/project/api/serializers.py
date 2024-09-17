from rest_framework.serializers import ModelSerializer
from app.models import Publisher, Author, Book

class PublisherSerializer(ModelSerializer):
    class Meta:
        model = Publisher
        fields = ('__all__')

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ('__all__')


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ('__all__')