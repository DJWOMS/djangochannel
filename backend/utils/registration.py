from rest_framework.exceptions import ValidationError

from djoser.views import UserCreateView
from djoser.serializers import UserCreateSerializer
from djoser.urls.base import User


class CustomUserCreateSerializer(UserCreateSerializer):
    """Сериализер создания юзера"""

    def validate(self, attrs):
        """
        Дописана логика проверки на пустое поле email
        и его уникальность
        """
        email = attrs.get('email')

        if not email:
            raise ValidationError({'email': 'Это поле обязательно.'})

        if User.objects.filter(email=email).exists():
            raise ValidationError(
                {'email': 'Пользователь с таким email уже существует.'}
            )

        super().validate(attrs)

        return attrs


class CustomUserCreateView(UserCreateView):
    """Переопределение сериализера на свой в наследуемой view"""
    serializer_class = CustomUserCreateSerializer
