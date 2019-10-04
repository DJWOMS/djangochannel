from django import template

register = template.Library()


@register.inclusion_tag('blog/tags/meta.html')
def meta(*objects):
    """Вывод description and title категории"""
    try:
        object = objects[0][0]
    except IndexError:
        object = []
    return {"object": object}
