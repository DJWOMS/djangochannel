from datetime import datetime

from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.views.generic import ListView, View
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from backend.forum.models import Category, Section, Topic, Message

from backend.forum.forms import MessageForm, CreateTopicForm


class Sections(ListView):
    """Вывод разделов форума"""
    model = Category
    template_name = "forum/section.html"


class TopicsList(ListView):
    """Вывод топиков раздела"""
    template_name = "forum/topics-list.html"

    def get_queryset(self):
        return Section.objects.filter(slug=self.kwargs.get("slug"))


class TopicDetail(ListView):
    """Вывод темы"""
    context_object_name = 'messages'
    template_name = 'forum/topic-detail.html'
    paginate_by = 10

    def get_queryset(self, queryset=None):
        return Message.objects.filter(topic__id=self.kwargs.get("pk"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["topic"] = Topic.objects.get(id=self.kwargs.get("pk"))
        context["form"] = MessageForm()
        return context


class EditTopic(LoginRequiredMixin, UpdateView):
    """Редактирование темы"""
    model = Topic
    form_class = MessageForm
    template_name = 'forum/update_message.html'


class EditMessages(LoginRequiredMixin, UpdateView):
    """Редактирование коментариев"""
    model = Message
    form_class = MessageForm
    template_name = 'forum/update_message.html'

    def form_valid(self, form):
        form.save()
        self.success_url = reverse_lazy('topic-detail', kwargs={"section": form.instance.topic.section,
                                                                "pk": form.instance.topic.id})
        return super().form_valid(form)

    def get_object(self, queryset=None):
        return Message.objects.get(id=self.kwargs.get("edit"))


class MessageCreate(LoginRequiredMixin, View):
    """Отправка комментария на форуме"""
    def post(self, request, section, pk):
        form = MessageForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.topic_id = pk
            form.save()
            return redirect("/forum/section/{}/{}/?page=last".format(section, pk))

# class MessageCreate(LoginRequiredMixin, CreateView):
#     """Создание темы на форуме"""
#     model = Message
#     form_class = MessageForm
#     template_name = 'forum/topic-detail.html'
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         form.instance.topic_id = self.kwargs.get("pk")
#         form.save()
#         return super().form_valid(form)


class CreateTopic(LoginRequiredMixin, CreateView):
    """Создание темы на форуме"""
    model = Topic
    form_class = CreateTopicForm
    template_name = 'forum/create-topic.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(CreateTopic, self).form_valid(form)
