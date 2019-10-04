from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.views.generic.base import View

from .models import CategoryTask, DCTask, Skills


class DCTaskList(View):
    """Вывожу все задания"""
    def get(self, request):
        tasks = DCTask.objects.all()
        return render(request, "dc_task/task-list.html", {"tasks": tasks})


class DCTaskDetail(View):
    """Подробнее о задании"""
    def get(self, request, category, slug):
        task = get_object_or_404(DCTask, slug=slug)
        return render(request, "dc_task/task-detail.html", {"task": task})


class Specialization(ListView):
    """Вывод специализаций и навыков"""
    model = CategoryTask
    template_name = "dc_task/special.html"


class AddSpecialUser(View):
    """Добавление спезиализации пользователю"""
    def get(self, request, pk):
        category = CategoryTask.objects.get(id=pk)
        if category.parent:
            spec_parent = get_object_or_404(Skills, user=request.user, skill_id=category.parent)
            if spec_parent.points >= category.points_need:
                special = Skills.objects.get_or_create(user=request.user, skill_id=pk)
        else:
            special = Skills.objects.get_or_create(user=request.user, skill_id=pk)
        return redirect("special")


