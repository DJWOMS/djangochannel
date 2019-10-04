from django import forms

from .models import Groups, EntryGroup, GroupLink


class GroupForm(forms.ModelForm):
    """Форма создания группы"""

    class Meta:
        model = Groups
        fields = ("title", "group_variety", "desc", "image", "miniature")


class EditGroupForm(forms.ModelForm):
    """Форма редактирования группы"""

    class Meta:
        model = Groups
        fields = ("title", "desc", "image", "miniature")


class RecordGroupForm(forms.ModelForm):
    """Форма добавления записи группы"""

    class Meta:
        model = EntryGroup
        fields = ("title", "text")


class LinkGroupForm(forms.ModelForm):
    """Форма добавления ссылок группы"""

    class Meta:
        model = GroupLink
        fields = ("title", "link")
