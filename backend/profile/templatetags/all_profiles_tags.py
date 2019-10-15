from django import template
from django.db.models import Q

from backend.profile.models import PersonalRecords

register = template.Library()

# @register.filter(takes_context=True)
# def if_friend(value, user):
#     """Проверка дружбы"""
#     return Followers.objects.filter(Q(subscribed_id=value) | Q(friends_id=value)). \
#         filter(Q(subscribed_id=user) | Q(friends_id=user)).filter(Q(in_friends=True) | Q(in_followers=True)).exists()


# @register.filter(takes_context=True)
# def if_followers(value, user):
#     """Проверка заявок на дружбу"""
#     return Followers.objects.filter(Q(subscribed_id=value) | Q(friends_id=value)). \
#         filter(Q(subscribed_id=user) | Q(friends_id=user)).filter(in_followers=True).exists()

@register.inclusion_tag('profile/public-personal-record.html')
def public_record_all(user):
    """Вывод публичных записей в профиле"""
    record_all = PersonalRecords.objects.filter(user=user, for_all=True)
    return {"record_all": record_all}


@register.inclusion_tag('profile/public-personal-record.html')
def public_record(pk, user):
    """Вывод записи для проверки в шаблоне"""
    record = PersonalRecords.objects.filter(Q(for_all=True) | Q(for_all=False)).filter(id=pk)
    print(record)
    you_record = False
    my_record = False
    one_record = record.first()
    print(one_record)
    if one_record.user.id == user.id:
        you_record = True
    elif one_record.user.id != user.id:
        my_record = False
    return {"record": record, "you_record": you_record, "my_record": my_record, "one_record": one_record}
