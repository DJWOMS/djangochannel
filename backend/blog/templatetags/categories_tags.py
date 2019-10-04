from django import template

from backend.blog.models import BlogCategory

register = template.Library()


@register.inclusion_tag('blog/tags/categories.html')
def menu_categories():
    """Вывод категортй блога"""
    return {"categories": BlogCategory.objects.filter(published=True)}
