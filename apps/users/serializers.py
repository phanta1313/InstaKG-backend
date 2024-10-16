from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)
    username = serializers.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'password',
            'confirm_password'
        ]

    def validate(self, data):
        if data['confirm_password'] != data['password']:
            data = []
            raise serializers.ValidationError('Passwords did not match!')
        return data 
    

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'password',
        ]