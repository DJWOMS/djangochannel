from django import template

from backend.courses.models import Category, Course

register = template.Library()


@register.inclusion_tag('courses/menu-courses.html')
def menu_courses():
    return {"categories": Category.objects.all()}


@register.inclusion_tag('courses/my-courses-count.html')
def my_course(user):
    return {"my_courses": Course.objects.filter(students=user, is_active=True).count()}
