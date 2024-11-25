from django.shortcuts import render
from rest_framework import generics
from .permissions import IsAdminUserForCreate
from rest_framework import viewsets
from .models import Book, Category, Author, Favorite
from .serializers import BookSerializer, AuthorSerializer, CategorySerializer, FavoriteSerializer
import os
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import FileResponse
from django.core.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from django.core.files.storage import default_storage
from rest_framework import status



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUserForCreate]
    
    @action(detail = True, methods=['get'], permission_classes=[IsAuthenticated], url_path='download')
    def download_book(self, request, pk=None):
        book = get_object_or_404(Book, pk=pk)

        book.download_count += 1
        book.save()
        
        if book.pdfLink:
            pdf_file = book.pdfLink
            file_path = pdf_file.name
            
            response = FileResponse(default_storage.open(file_path, 'rb'), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
            
            return response
        else:
            return Response({"error": "PDF file not found."}, status=404)
            
            
    @action(detail=True, methods=['get'], permission_classes=[AllowAny], url_path='read_online')
    def server_pdf_open(self, request, pk=None):
        book = get_object_or_404(Book, pk=pk)
        
        if book.pdfLink:
            pdf_file = book.pdfLink
            response = FileResponse(pdf_file.open("rb"),  content_type="application/pdf") #will keep it simple with pdf but
                                                                                            #if u want to serve different file types, explore  "mime" library
            response['Content-Disposition'] = 'inline; filename="{}"'.format(book.title)
            return response
        
        else:
            return Response({"error": "PDF file not found."}, status=404)
        
        
    @action(detail=True, methods=['delete','post'], permission_classes=[IsAuthenticated], url_path="favorites")
    def manage_favorites(self, request, pk=None):
        user = request.user
        book = get_object_or_404(Book, pk=pk)
        
        if request.method == "POST":
            if Favorite.objects.filter(user=user, book=book).exists():
                return Response({"detail":"Book already in favorites"}, status=400)
            Favorite.objects.create(user=user, book=book)
            return Response({"detail":"Book added to favorites"}, status=201)
            
        elif request.method == "DELETE":
            favorite = Favorite.objects.create(user=user, book=book)
            if not favorite:
                return Response({"detail":"Book not in favorites"}, status=400)
            favorite.delete()
            return Response({"detail":"Book removed from favorites"}, status=204)
            
    @action(detail=False, methods=['get'], url_path="search")
    def search(self, request):
        query = request.query_params.get('q', None)
        if query:
            results = Book.objects.filter(title__icontains=query) | \
                    Book.objects.filter(author__name__icontains=query) | \
                    Book.objects.filter(description__icontains=query) | \
                    Book.objects.filter(category__name__icontains=query)
            serializer = self.get_serializer(results, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error":"query parameter 'q' is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        
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
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Favorite.objects.filter(user=self.request.user)
        return Favorite.objects.none()
    
    
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
    

    