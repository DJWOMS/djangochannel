from rest_framework import generics, permissions

from backend.courses.models import Course
from backend.api.v2.courses.serializers import CourseSerializer


class CourseView(generics.ListAPIView):
    """Вывод списка курсов"""
    permission_classes = [permissions.AllowAny]
    serializer_class = CourseSerializer

    def get_queryset(self):
        count = self.request.GET.get("count", None)
        courses = Course.objects.filter(is_active=True, is_complete=False)
        if count is not None:
            courses = courses.order_by()[:int(count)]
        return courses

