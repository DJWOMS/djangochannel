from rest_framework import serializers

from django.contrib.auth.models import User

from backend.profile.models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    """Сериализация пользователя"""
    class Meta:
        model = User
        fields = ("id", "username")


class UserProfileSerializer(serializers.ModelSerializer):
    """Сериализация профиля пользователя"""
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ("user", "cover", "image")


class UserProfilePublicSerializer(serializers.ModelSerializer):
    """Сериализация публичного профиля пользователя"""
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ("user", "cover", "image")

