from rest_framework import serializers

from backend.api.v2.profile.serializers import UserForProfileSerializer
from backend.reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализация отзывов"""
    user = UserForProfileSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ("user", "name", "text", "social_link", "git_link")

