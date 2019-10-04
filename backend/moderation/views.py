from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from backend.moderation.models import BannedUser
from backend.moderation.permissions import IsModerator

User = get_user_model()


class AboutModerator(APIView):
    """
    Возвращает инфо, является ли юзер модератором,
    и если да, то какие права имеет
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response(self.about_moderator(request.user))

    @staticmethod
    def about_moderator(user):
        if user.profile.is_forum_moderator:
            return {
                'moderator': True,
                'rights': [x.key for x in user.moderator_rights.rights.all()]
            }
        return {'moderator': False}


class BanUser(APIView):
    """
    Выдача бана пользователю,
    принимаемые параметры:
        action: числовой идентификатор запрещаемого действия,
        от 1 до 3;
        user_id: id юзера, которого хотим забанить.

    Список actions:
        1: 'Запретить комментирование',
        2: 'Запретить создание топиков',
        3: 'Запретить доступ к форуму'
    """
    permission_classes = [IsModerator]

    def post(self, request):
        ban_action = int(request.data.get('action', None))
        user_id = request.data.get('user_id', None)

        if not ban_action or not user_id:
            return Response('Не указаны action или user_id')

        check_rights = AboutModerator().about_moderator(request.user)

        if 0 not in check_rights['rights']:
            if ban_action not in check_rights['rights']:
                return Response({'detail': 'Нет полномочий'}, status=403)

        user = User.objects.get(id=user_id)

        if not BannedUser.objects.filter(user=user, ban_action=ban_action).exists():
            BannedUser.objects.create(
                user=user, ban_action=ban_action, moderator=request.user)
            return Response('Пользователь {} забанен'.format(user_id))

        return Response('Пользователь {} уже забанен'.format(user_id))
