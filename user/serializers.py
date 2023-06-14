from rest_framework import serializers
from .models import CustomUser, Adress
from django.core import exceptions
import django.contrib.auth.password_validation as validators

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'phone', 'password', 'is_staff', 'verify_code']

    def validate(self, data):
        user = CustomUser(**data)
        password = data.get('password')
        errors = dict()
        try:
            validators.validate_password(password=password, user=user)
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)
        if errors:
            raise serializers.ValidationError(errors)
        return super(RegistrationSerializer, self).validate(data)

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        user.generate_code
        return user


class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=13)
    password = serializers.CharField(max_length=50)


class ChangePasswordSerializer(serializers.Serializer):
    model = CustomUser

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "phone", "username", "is_staff", "image", "email", "birthday", "passport_series", "passport_number", 'image', 'data_joined']


class AdressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adress
        fields = '__all__'