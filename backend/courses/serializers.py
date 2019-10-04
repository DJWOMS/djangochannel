from rest_framework import serializers
from .models import Category, Course, Task, RealizationTask

#  Сериализеры категории


class CategorySerializer(serializers.ModelSerializer):
    """Сериализация категории"""
    class Meta:
        model = Category
        fields = ('id', 'title', 'image')


class MinCategorySerializer(serializers.ModelSerializer):
    """Минимальная сериализация категории"""
    class Meta:
        model = Category
        fields = ('id', 'title')

#  Сериализеры курса


class MinimalCourseSerializer(serializers.ModelSerializer):
    """Минимальная сериализация курса"""
    class Meta:
        model = Course
        fields = ('id', 'title')


class ImageCourseSerializer(serializers.ModelSerializer):
    """Минимальная сериализация курса с картинкой"""
    class Meta:
        model = Course
        fields = ('id', 'title', 'image')


class PriceCourseSerializer(serializers.ModelSerializer):
    """Сериализация курса с ценой"""
    class Meta:
        model = Course
        fields = ('id', 'price')


class CourseSerializer(serializers.ModelSerializer):
    """Сериализация курса"""
    class Meta:
        model = Course
        fields = ('id', 'title', 'description')


class OutputCourseSer(serializers.ModelSerializer):
    """Сериализация описания курса"""
    category = MinCategorySerializer()

    class Meta:
        model = Course
        fields = (
            'id', 'title', 'description',
            'image', 'category', 'price',
            'date_start', 'program', 'target_audience',
            'requirements', 'available', 'count_seats',
            'date_end', 'count_students', 'lessons_on_weak',
            'lessons_time',
        )


class FullCourseSerializer(serializers.ModelSerializer):
    """Полная сериализация курса"""
    class Meta:
        model = Course
        fields = '__all__'


#  Сериализеры задания


class MinimalTaskSerializer(serializers.ModelSerializer):
    """Минимальная сериализация задания"""
    class Meta:
        model = Task
        fields = ('id', 'title')


class FullTaskSerializer(serializers.ModelSerializer):
    """Полная сериализация задания"""
    course = PriceCourseSerializer()

    class Meta:
        model = Task
        fields = '__all__'


#  Сериализеры выполнения задания


class MinRealizationTaskSerializer(serializers.ModelSerializer):
    """Минимальная сериализация выполнения задания"""
    class Meta:
        model = RealizationTask
        fields = ('task', 'answer')


class PatchRealizationTaskSerializer(serializers.ModelSerializer):
    """Сериализация выполнения задания для изменения ответа"""
    class Meta:
        model = RealizationTask
        fields = ('answer',)


class FullRealizationTaskSerializer(serializers.ModelSerializer):
    """Полная сериализация выполнения задания"""
    class Meta:
        model = RealizationTask
        fields = '__all__'


class RealizationTaskSerializer(serializers.ModelSerializer):
    """Сериализация выполнения задания для описания задания"""
    class Meta:
        model = RealizationTask
        fields = ("id", 'answer', 'comment', 'success')
