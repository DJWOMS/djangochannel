from django.shortcuts import render
from django.views.generic import View, ListView

from .models import Test, Question


class ListTests(ListView):
    """Список тестов"""
    queryset = Test.objects.filter(active=True, in_course=False, course__test_in_course__isnull=True)
    template_name = "dc_tests/list-tests.html"


class DetailTest(View):
    """Прохождение теста"""
    def get(self, request, pk):
        test = Test.objects.get(id=pk)
        return render(request, 'dc_tests/detail-test.html', {"test": test})