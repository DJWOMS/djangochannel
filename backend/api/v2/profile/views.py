from rest_framework import generics, permissions
from backend.profile.models import UserProfile
from backend.api.v2.profile.serializers import UserProfileSerializer, UserProfilePublicSerializer


class ProfileView(generics.ListAPIView):
    """Вывод профиля"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)


class ProfilePublicView(generics.RetrieveAPIView):
    """Вывод публичныого профиля"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserProfilePublicSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(public=True)

