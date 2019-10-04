from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    """Форма комментариев статьи"""

    class Meta:
        model = Comment
        fields = ("text", )


class UserPostForm(forms.ModelForm):
    """Форма пользовательской статьи"""

    class Meta:
        model = Post
        fields = ("title", "category", "tag", "mini_text", "text",)
