from django import template

from backend.blog.models import Comment

register = template.Library()


@register.inclusion_tag('blog/tags/comments.html', takes_context=True)
def comments_show(context, pk):
    """Вывод комментариев к статье"""
    return {"comments": Comment.objects.filter(post_id=pk, published=True), "context": context}
