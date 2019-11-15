from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from backend.profile.models import UserProfile
from backend.api.v2.profile.serializers import UserProfileSerializer, UserProfilePublicSerializer


class ProfileView(generics.RetrieveAPIView):
    """Вывод личного профиля"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = UserProfile.objects.filter(public=True)
    serializer_class = UserProfileSerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, user=self.request.user)
        self.check_object_permissions(self.request, obj)
        return obj


class PublicProfileView(generics.RetrieveAPIView):
    """Вывод публичныого профиля"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = UserProfile.objects.filter(public=True)
    serializer_class = UserProfilePublicSerializer

