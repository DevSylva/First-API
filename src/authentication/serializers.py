from rest_framework import serializers
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        first_name = attrs.get('first_name', '')
        last_name = attrs.get('last_name', '')

        if not username.isalnum():
            raise serializers.ValidationError('The username should only contain alphanumeric characters')
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class EmailVerificationSerializer(serializers.ModelSerializer):
    token=serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields=['token']

class LoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255, min_length=3)
    first_name = serializers.CharField(max_length=255, read_only=True)
    last_name = serializers.CharField(max_length=255, read_only=True)
    password=serializers.CharField(max_length=68, min_length=6)
    username=serializers.CharField(max_length=255, min_length=6, read_only=True)
    tokens=serializers.CharField(max_length=68, min_length=6, read_only=True)

    class Meta:
        model=User
        fields=['email','password','username','tokens','first_name','last_name']

    def validate(self, attrs):
        email=attrs.get('email', '')
        password = attrs.get('password', '')

        class Meta:
            model = User
            fields = ['email','password','tokens']

        user=auth.authenticate(email=email,password=password)
        if not user:
            raise AuthenticationFailed('Invalid Credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account Disabled, contact an Admin')
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified')

        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.token,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }
        return super().validate(attrs)