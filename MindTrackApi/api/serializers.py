from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from api.models import User

class UserSerializer(serializers.ModelSerializer):
    username = serializers.EmailField(source='email')  # Use email as username

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}  # Specify that password is write-only

    def create(self, validated_data):
        validated_data['username'] = validated_data.get('email')  # Set username to email
        validated_data['password'] = make_password(validated_data.get('password'))  # Hash the password
        return super(UserSerializer, self).create(validated_data)
