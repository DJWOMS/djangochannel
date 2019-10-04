from django import template

from backend.message.models import PrivatMessages

register = template.Library()


@register.inclusion_tag('message/not_read_mess_all.html')
def not_read_mess_all(user):
    """Все не прочитанные сообщения"""
    return {"count_mess": PrivatMessages.objects.filter(
                                        room__recipient=user, read=False).exclude(user=user).count()
            }


@register.inclusion_tag('message/not_read_mess_all.html')
def not_read_mess_room(id, user):
    """Все не прочитанные сообщения комнаты"""
    return {"count_mess": PrivatMessages.objects.filter(room_id=int(id), read=False).exclude(user=user).count()}
