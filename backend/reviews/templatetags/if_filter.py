from django import template

register = template.Library()


@register.filter
def if_int_entirely(value):
    """Фильтр проверки на целое число"""
    return int(value/2) == float(value/2)