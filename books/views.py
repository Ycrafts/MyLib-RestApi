from django.shortcuts import render
from rest_framework import generics
from .models import Book, Category, Author, FavoriteList
from .serializers import BookSerializer, AuthorSerializer, CategorySerializer, FavoriteListSerializer

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class FavoriteListList(generics.ListCreateAPIView):
    queryset = FavoriteList.objects.all()
    serializer_class = FavoriteListSerializer
    
class FavoriteListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FavoriteList.objects.all()
    serializer_class = FavoriteListSerializer
    