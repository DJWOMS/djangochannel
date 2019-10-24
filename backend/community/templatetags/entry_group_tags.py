from django import template

from backend.community.models import EntryGroup, GroupLink

register = template.Library()


@register.inclusion_tag("community/tags/all-entry.html")
def all_entry(pk):
    """Вывод записей группы"""
    return {"entry": EntryGroup.objects.filter(group__id=pk)}


@register.inclusion_tag("community/tags/all-entry.html")
def all_link(pk):
    """Вывод ссылок группы"""
    return {"links": GroupLink.objects.filter(group__id=pk)}
