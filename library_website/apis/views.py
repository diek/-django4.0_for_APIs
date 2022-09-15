from books.models import Book
from django.shortcuts import render
from rest_framework import generics

from .serializers import BookSerializer


class BookAPIView(generics.ListAPIView):
    # create a read-only endpoint for all book instances
    queryset = Book.objects.all()
    serializer_class = BookSerializer
