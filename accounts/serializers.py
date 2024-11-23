from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
        )
        model = get_user_model()
        
    
    