from django import forms

from .models import Room, PrivatMessages


class RoomForm(forms.ModelForm):
    """Форма комнаты личных сообщений"""
    class Meta:
        model = Room
        fields = ("recipient", )


class MessageForm(forms.ModelForm):
    """Форма личных сообщений"""
    class Meta:
        model = PrivatMessages
        fields = ("text",)