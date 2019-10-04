from rest_framework import serializers
from .models import TestCategory, Test, Question, PossibleAnswer


class TestCategorySerializer(serializers.ModelSerializer):
    """Сериализация категории тестов"""
    class Meta:
        model = TestCategory
        fields = ('title',)


class TestSerializer(serializers.ModelSerializer):
    """Сериализация тестов"""
    class Meta:
        model = Test
        fields = ('id', 'title', 'category')


class QuestionSerializer(serializers.ModelSerializer):
    """Сериализация вопросов"""
    class Meta:
        model = Question
        fields = ('id', 'text', 'desc', 'test')


class PossibleAnswerSerializer(serializers.ModelSerializer):
    """Сериализация вариатнов ответа"""
    question = QuestionSerializer()

    class Meta:
        model = PossibleAnswer
        fields = ('id', 'text', 'question')
