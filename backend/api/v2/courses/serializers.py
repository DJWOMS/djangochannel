from rest_framework import serializers

from backend.courses.models import Course, Category


class ListCategoryCourseSerializer(serializers.ModelSerializer):
    """Сериализация списка категорий курсов"""

    class Meta:
        model = Category
        fields = ("id", "title", "slug")


class ListCourseSerializer(serializers.ModelSerializer):
    """Сериализация списка курсов"""

    class Meta:
        model = Course
        fields = ("id", "title", "description", "date_start", "date_end", "get_absolute_url")


class DetailCourseSerializer(serializers.ModelSerializer):
    """Сериализация описания курса"""

    def check(self, *args, **kwargs):
        pass

    class Meta:
        model = Course
        exclude = ("students", "test_in_course")


