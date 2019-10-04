from django import template
from django.db.models import Q

from backend.followers.models import Followers

register = template.Library()


@register.inclusion_tag('followers/all-user-count.html')
def friend_request(user):
    """Все заявки в друзья"""
    return {"count_friends": Followers.objects.filter(subscribed=user,
                                                      in_friends=False,
                                                      in_followers=False).count()}


@register.inclusion_tag('followers/all-user-count.html')
def friend_count(user):
    """Колличество друзей"""
    return {"friends_all": Followers.objects.filter(Q(subscribed_id=user) |
                                                    Q(friends_id=user)).filter(
                                                    Q(subscribed_id=user) |
                                                    Q(friends_id=user)).filter(in_friends=True).count()}


@register.inclusion_tag('followers/all-user-count.html')
def followers_count(user):
    """Колличество подписчиков"""
    return {"followers_all": Followers.objects.filter(subscribed_id=user, in_followers=True).count()}


@register.inclusion_tag('followers/checking-friends.html')
def friends_of_follower(pk, user):
    """Вывод записи для проверки в шаблоне"""
    follower = Followers.objects.filter(Q(subscribed_id=pk) |
                                        Q(friends_id=pk)).filter(
                                        Q(subscribed_id=user) |
                                        Q(friends_id=user))
    is_friend = False
    is_follow = False
    petition = False
    cancel_petition = False

    if follower.exists():
        follower = follower.first()
        check = (follower.subscribed_id == user.id and follower.friends_id == pk) \
                or (follower.friends_id == user.id and follower.subscribed_id == pk)
        if check and follower.in_friends == True:
            is_friend = True
        elif check and follower.in_followers == True:
            is_follow = True
        elif follower.friends_id == user.id and follower.subscribed_id == pk:
            petition = True
        elif (follower.subscribed_id == user.id and follower.friends_id == pk) \
             and (follower.in_friends == False and follower.in_followers == False):
            cancel_petition = True
        else:
            cancel_petition = False
    return {"follower": follower, "pk": pk, "user": user, "is_friend": is_friend,
            "is_follow": is_follow, "petition": petition, "cancel_petition": cancel_petition}
