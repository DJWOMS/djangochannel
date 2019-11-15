from rest_framework import generics, permissions
from backend.reviews.models import Review
from backend.api.v2.reviews.serializers import ReviewSerializer


class ReviewView(generics.ListCreateAPIView):
    """Вывод и добавление отзывов"""
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Review.objects.filter(moderated=True)
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
