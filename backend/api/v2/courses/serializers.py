from rest_framework import serializers

from backend.courses.models import Course


class CourseSerializer(serializers.ModelSerializer):
    """Сериализация курсов"""

    class Meta:
        model = Course
        fields = ("id", "title", "description", "date_start", "date_end", "get_absolute_url")


