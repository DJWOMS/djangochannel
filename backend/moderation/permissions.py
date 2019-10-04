"""

Для проверки прав модератора на доступ к определенной APIView
импортировать из данного файла (moderation/permissions.py)
нужный permission, после указать его в permission_classes APIView.

Пример:


from rest_framework.views import APIView

from moderation.permissions import IsModerator

class MyView(APIView):
    permission_classes = [IsModerator]

    def get(self):
        pass

    def post(self):
        pass

    Таким образом все методы этого класса
    будут доступны только модератору.


Также можно указать доступ к отдельной функции:


from rest_framework.views import APIView
from rest_framework import permissions

from utils.decorators import permissions as perms
from moderation.permissions import IsModerator

class MyView(APIView):
    permission_classes = [permissions.AllowAny]

    @perms(IsModerator)
    def get(self):
        pass

    def post(self):
        pass


    Таким образом метод get() будет доступен
    только модератору, а все остальные методы
    будут общедоступными.

"""

from rest_framework.permissions import BasePermission

from .models import SimpleRight


COMMENTING_BAN = (
    0,
    1,
)

CREATE_TOPICS_BAN = (
    0,
    2,
)

ACCESS_TO_FORUM_BAN = (
    0,
    3,
)

EDITING_TOPICS = (
    0,
    4
)

DELETE_TOPICS = (
    0,
    5
)

DELETE_MESSAGES = (
    0,
    6
)

consts = [COMMENTING_BAN, CREATE_TOPICS_BAN, ACCESS_TO_FORUM_BAN, EDITING_TOPICS, DELETE_TOPICS, DELETE_MESSAGES]


class IsModerator(BasePermission):
    """Доступ модератору"""
    def has_permission(self, request, view):
        return request.user.profile.is_forum_moderator


class BaseModeratorPermission(BasePermission):
    """Базовый класс для проверки модераторских полномочий"""
    actions = ()

    def has_permission(self, request, view):
        if request.user.profile.is_forum_moderator:
            rights = SimpleRight.objects.filter(key__in=self.actions)
            return any(r in request.user.moderator_rights.rights.all() for r in rights)
        return False


class CanBanComments(BaseModeratorPermission):
    """
    Возможность бана на создание комментариев
    """
    actions = COMMENTING_BAN


class CanBanCreateTopics(BaseModeratorPermission):
    """
    Возможность бана на создание топиков
    """
    actions = CREATE_TOPICS_BAN


class CanBanAccessForum(BaseModeratorPermission):
    """Возможность бана на доступ к форуму"""
    actions = ACCESS_TO_FORUM_BAN


class CanEditTopics(BaseModeratorPermission):
    """Возможность редактировать топики"""
    actions = EDITING_TOPICS


class CanDeleteTopics(BaseModeratorPermission):
    """Возможность удалять топики"""
    actions = DELETE_TOPICS


class CanDeleteMessages(BaseModeratorPermission):
    """Возможность удалять сообщения"""
    actions = DELETE_MESSAGES
