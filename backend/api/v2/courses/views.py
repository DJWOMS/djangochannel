from rest_framework import generics, permissions
from rest_framework.response import Response

from backend.courses.models import Course, Category
from backend.api.v2.courses.serializers import (
    ListCourseSerializer, ListCategoryCourseSerializer, DetailCourseSerializer
)


class ListCategoryView(generics.ListAPIView):
    """Вывод списка сатегорий курсов"""
    permission_classes = [permissions.AllowAny]
    queryset = Category.objects.all()
    serializer_class = ListCategoryCourseSerializer


class CourseView(generics.ListAPIView):
    """Вывод списка курсов"""
    permission_classes = [permissions.AllowAny]
    serializer_class = ListCourseSerializer

    def get_queryset(self):
        count = self.request.GET.get("count", None)
        courses = Course.objects.filter(is_active=True, is_complete=False)
        if count is not None:
            courses = courses.order_by()[:int(count)]
        return courses


class CourseDetailView(generics.RetrieveAPIView):
    """Вывод оптсантия курса и добавление на курс"""
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Course.objects.filter(is_active=True, is_complete=False)
    serializer_class = DetailCourseSerializer

    def post(self, request, **kwargs):
        course = self.get_object()
        if course.price == 0:
            course.students.add(request.user)
            return Response(status=201)
        else:
            return Response(status=400)


