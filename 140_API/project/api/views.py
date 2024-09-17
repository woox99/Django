from rest_framework import generics
from app.models import Publisher, Author, Book
from .serializers import PublisherSerializer, AuthorSerializer, BookSerializer


class PublisherList(generics.ListCreateAPIView):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()


class PublisherDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()

    
class AuthorList(generics.ListCreateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

    
class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorSerializer
    queryset = Publisher.objects.all()


class BookList(generics.ListCreateAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        publisher = self.request.query_params.get('publisher')
        if publisher is not None:
            queryset = queryset.filter(publisher=publisher)
        return queryset


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()