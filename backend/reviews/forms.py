from django import forms

from .models import Review


class ReviewsForm(forms.ModelForm):
    """Форма добавления отзыва"""
    class Meta:
        model = Review
        fields = ["name", "text", "social_link", "git_link"]
        labels = {
            "name": (""),
            "text": (""),
            # "social_link": (""),
            # "git_link": ("")
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ваше имя'}),
            'text': forms.Textarea(attrs={'placeholder': 'Текст отзыва'}),
        }
