from rest_framework import serializers
from .models import Book,Category, FavoriteList, Author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "title",
            "author",
            "pdfLink",
            "publicationDate",
            "coverImage",
            "category",
            "download_count",
        )
        model = Book

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            "name",
            "description",
        )
        model = Category

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "name",
        )
        model = Author
        
class FavoriteListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "user",
            "book",
        )
        model = FavoriteList