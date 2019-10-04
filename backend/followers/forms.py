from django import forms

from .models import Followers


class FollowersForm(forms.ModelForm):
    """Форма добавления в друзья"""
    class Meta:
        model = Followers
        fields = ()
