from django import forms

# from backend.dc_tests.models import Test, Question
from .models import MessagesTask


class AnswerTaskForm(forms.ModelForm):
    """Форма ответа на задание"""
    class Meta:
        model = MessagesTask
        fields = ("answer", )


# class TaskForm(forms.Form):
#
#     test = forms.ModelChoiceField(
#         queryset=Test.objects.all(),
#         widget=ModelSelect2Widget(
#             model=Test,
#         )
#     )
#
#     questions = forms.ModelMultipleChoiceField(
#         queryset=Question.objects.all(),
#         widget=ModelSelect2MultipleWidget(
#             model=Question,
#             dependent_fields={'test': 'test'},
#             max_results=100
#         )
#     )
