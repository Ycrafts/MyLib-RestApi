from django.shortcuts import render
from rest_framework import generics
from .permissions import IsAdminUserForCreate
from rest_framework import viewsets
from .models import Book, Category, Author, Favorite
from .serializers import BookSerializer, AuthorSerializer, CategorySerializer, FavoriteSerializer

    
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUserForCreate]
class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUserForCreate]
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserForCreate]
class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAdminUserForCreate]
# class BookList(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class BookDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class AuthorList(generics.ListCreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

# class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
    
# class CategoryList(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
    
# class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
    
# class FavoriteList(generics.ListCreateAPIView):
#     queryset = Favorite.objects.all()
#     serializer_class = FavoriteSerializer
    
# class FavoriteDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Favorite.objects.all()
#     serializer_class = FavoriteSerializer
    

    