from django.shortcuts import render
from .serializers import CustomUserSerializer
from rest_framework import viewsets
from .models import CustomUser
from .permissions import IsOwnerOrAdmin

class CustomUserViewset(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsOwnerOrAdmin]
    
    