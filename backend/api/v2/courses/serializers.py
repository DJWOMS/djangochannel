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

    is_student = serializers.SerializerMethodField()

    def get_is_student(self, obj):
        """Проверка является ли юзер студентом курса"""
        if self.context.get("request", None):
            if self.context['request'].user in self.instance.students.all():
                return True

    class Meta:
        model = Course
        exclude = ("students", "test_in_course")


