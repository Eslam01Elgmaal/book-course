import re
from rest_framework import serializers
from .models import Student
from django.contrib.auth import authenticate

# Creating Student Registration Serializer
class StudentRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = Student
        fields = ['username','first_name', 'last_name', 'email', 'phone_number', 'password', 'confirm_password']
    
    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        if len(password) < 8:
            raise serializers.ValidationError({"password": "Password must be at least 8 characters."})

        if not re.search(r"[0-9]", password):
            raise serializers.ValidationError({"password": "Password must contain at least one number."})

        if not re.search(r"[A-Z]", password):
            raise serializers.ValidationError({"password": "Password must contain at least one uppercase letter."})

        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            raise serializers.ValidationError({"password": "Password must contain at least one symbol."})

        if not re.fullmatch(r"[A-Za-z0-9!@#$%^&*(),.?\":{}|<>]+", password):
            raise serializers.ValidationError({"password": "Password must contain only English letters, numbers, and symbols."})

        return attrs

    def create(self, validated_data):
        user = Student.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            password=validated_data['password'],
        )
        return user

# Creating Student Login Serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(username=attrs['username'], password=attrs['password'])
        if not user:
            raise serializers.ValidationError("username or password is incorrect")
        attrs['user'] = user
        return attrs
