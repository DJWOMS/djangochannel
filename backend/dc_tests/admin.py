from django.contrib import admin
from django import forms

from .models import TestCategory, Test, Question, PossibleAnswer, AnswersCounter
from backend.utils.admin import all_fields


class AdminQuestionForm(forms.ModelForm):
    """
    Форма для админки вопросов,
    добавлена проверка на обязательное
    указание верного варианта
    """
    class Meta:
        model = Question
        fields = '__all__'

    def clean(self):
        if 'on' not in self.get_variants():
            msg = 'Выберите верный вариант'
            self.add_error(None, msg)

        return super().clean()

    def get_variants(self):
        for k, v in self.data.items():
            if 'is_right' in k:
                yield v


# Models

class AdminQuestion(admin.ModelAdmin):
    """Админка вопросов"""

    class PossibleAnswerInline(admin.TabularInline):
        """
        Возможность добавления вариантов ответа
        сразу при создании вопроса
        """
        model = PossibleAnswer

    form = AdminQuestionForm
    inlines = [
        PossibleAnswerInline,
    ]
    list_display = ("id", "text", "test")
    list_display_links = ("text",)


class AdminTest(admin.ModelAdmin):
    """Админка тестов"""
    class QuestionInline(admin.TabularInline):
        """
        Возможность добавления вопросов
        сразу при создании теста
        """
        model = Question
    list_display = all_fields(Test)
    inlines = [
        QuestionInline,
    ]


class AdminPossibleAnswer(admin.ModelAdmin):
    """Админка вариантов ответа"""
    list_display = all_fields(PossibleAnswer)


class AnswersCounterAdmin(admin.ModelAdmin):
    """Ответы на тесты"""
    list_display = all_fields(AnswersCounter)


admin.site.register(TestCategory)
admin.site.register(Test, AdminTest)
admin.site.register(Question, AdminQuestion)
admin.site.register(PossibleAnswer, AdminPossibleAnswer)
admin.site.register(AnswersCounter, AnswersCounterAdmin)
