from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Groups, EntryGroup, GroupLink
from .forms import GroupForm, EditGroupForm, RecordGroupForm, LinkGroupForm


class GroupList(LoginRequiredMixin, ListView):
    """Список всех открытых и закрытых групп"""

    model = Groups
    template_name = "community/group-list.html"

    def get_queryset(self):
        return self.model.objects.filter(
            Q(group_variety="open") | Q(group_variety="closed")
        )


class GroupDetail(LoginRequiredMixin, DetailView):
    """Детально о группе"""

    model = Groups
    context_object_name = "group"
    template_name = "community/group-detail.html"


class CreateGroup(LoginRequiredMixin, CreateView):
    """Создание группы, команды"""

    model = Groups
    form_class = GroupForm
    template_name = "community/create-group.html"

    def form_valid(self, form):
        form.instance.founder = self.request.user
        form.save()
        return super(CreateGroup, self).form_valid(form)


class RemoveGroup(LoginRequiredMixin, DeleteView):
    """Удаление группы"""

    model = Groups
    template_name = "community/delete-group.html"
    success_url = reverse_lazy("profile")


class EditGroup(LoginRequiredMixin, UpdateView):
    """Редактирование группы"""

    model = Groups
    template_name = "community/create-group.html"
    form_class = EditGroupForm


class CreateRecordGroup(LoginRequiredMixin, CreateView):
    """Добавление записи в группе"""

    model = EntryGroup
    form_class = RecordGroupForm
    template_name = "community/create-group.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.group_id = self.kwargs.get("pk")
        self.success_url = reverse_lazy(
            "detail_groups", kwargs={"pk": self.kwargs.get("pk")}
        )
        form.save()
        return super(CreateRecordGroup, self).form_valid(form)


class EditRecordGroup(LoginRequiredMixin, UpdateView):
    """Редактирование записи группы"""

    model = EntryGroup
    template_name = "community/create-group.html"
    form_class = RecordGroupForm


class RemoveRecordGroup(LoginRequiredMixin, DeleteView):
    """Удаление записи группы"""

    model = EntryGroup
    template_name = "community/delete-group.html"
    success_url = reverse_lazy("all_groups")


class CreateLinkGroup(LoginRequiredMixin, CreateView):
    """Добавление ссылки в группе"""

    model = GroupLink
    form_class = LinkGroupForm
    template_name = "community/create-group.html"

    def form_valid(self, form):
        form.instance.group_id = self.kwargs.get("pk")
        form.save()
        return super(CreateLinkGroup, self).form_valid(form)


class EnterGroup(LoginRequiredMixin, UpdateView):
    """Вступление в группу"""

    model = Groups
    fields = ("members",)
    template_name = "community/group-detail.html"

    def get_queryset(self):
        group = self.model.objects.filter(id=self.kwargs.get("pk"))
        new = group.first()
        new_member = new.members.add(self.request.user)
        self.success_url = reverse_lazy(
            "detail_groups", kwargs={"pk": self.kwargs.get("pk")}
        )
        return group
