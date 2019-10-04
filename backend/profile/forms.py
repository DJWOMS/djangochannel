from django import forms

from .models import UserProfile, PersonalRecords


class ProfileForm(forms.ModelForm):
    """Форма редактирования профиля"""
    class Meta:
        model = UserProfile
        fields = ("image",)
        widgets = {"image": forms.FileInput()}


class PersonalRecordsForm(forms.ModelForm):
    """Форма добавления записи в дневник"""
    class Meta:
        model = PersonalRecords
        fields = ("title", "note", "for_all")
