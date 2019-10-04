from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    """Форма обратной связи"""
    class Meta:
        model = Contact
        fields = ("__all__")