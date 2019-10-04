from django import forms
from backend.forum.models import Message, Topic


class MessageForm(forms.ModelForm):
    """Форма комментариев на форуме"""

    class Meta:
        model = Message
        fields = ("text", )


class CreateTopicForm(forms.ModelForm):
    """Форма создания топика форума"""
    class Meta:
        model = Topic
        fields = ("title", "section", "text")
        labels = {
            # "title": (""),
            "text": ("")
        }