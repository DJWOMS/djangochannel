from datetime import timedelta, datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, Http404

from django.db.models import Q, F
from django.urls import reverse_lazy
from django.views.generic.dates import BaseDateListView

from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post, SpySearch, Comment
from .forms import CommentForm, UserPostForm


class PostList(ListView):
    """Список всех статей и по категории"""
    paginate_by = 12
    template_name = "blog/post-list.html"

    def get_queryset(self):
        if self.kwargs.get("category") is not None:
            posts = Post.objects.filter(category__slug=self.kwargs.get('category'))
        elif self.kwargs.get("tag") is not None:
            posts = Post.objects.filter(tag__slug=self.kwargs.get('tag'))
        else:
            posts = Post.objects.filter(published=True)
        return posts


class SinglePost(DetailView):
    """Полная статья"""
    model = Post
    context_object_name = 'post'

    def get_queryset(self):
        query = Post.objects.filter(slug=self.kwargs.get("slug"))
        for a in query:
            a.viewed += 1
            a.save()
        return query


class SearchPost(ListView):
    """Поиск в блоге"""
    paginate_by = 5
    template_name = "blog/post-list.html"

    def get_queryset(self):
        query = Post.objects.filter(title__icontains=self.request.GET.get('q'))

        question = self.request.GET.get('q')
        rec, a = SpySearch.objects.get_or_create(record=question)
        rec.counter += 1
        rec.save()
        return query


class DayWeekMonth(ListView):
    """Сортировка по дню, неделе, месяцу"""
    paginate_by = 5
    template_name = "blog/post-list.html"

    def get_queryset(self):
        if self.request.GET.get('d'):
            sorts = Post.objects.filter(published_date__date=self.request.GET.get('d'))
        elif self.request.GET.get('w'):
            sorts = Post.objects.filter(published_date__week=self.request.GET.get('w'))
        else:
            sorts = Post.objects.filter(
                Q(published_date__year=self.request.GET.get('y')) &
                Q(published_date__month=self.request.GET.get('m')))
        return sorts


class CommentCreate(LoginRequiredMixin, CreateView):
    """Отправка комментария к статье"""
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comments-create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post_id = self.kwargs.get('pk')
        self.success_url = form.instance.post.get_absolute_url()
        form.save()
        return super(CommentCreate, self).form_valid(form)


class EditComment(LoginRequiredMixin, UpdateView):
    """Редактирование комментария"""
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comments-create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.id = self.kwargs.get('pk')
        self.success_url = form.instance.post.get_absolute_url()
        form.save()
        return super(EditComment, self).form_valid(form)


class AnswerComment(LoginRequiredMixin, CreateView):
    """Ответ на комментарий"""
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comments-create.html'

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.post = Post.objects.get(comment=self.kwargs.get('pk'))
            comm_1 = self.model.objects.get(id=self.kwargs.get('pk'))
            form.text = comm_1.user.username + ',' + form.text
            form.save()
            form.move_to(comm_1)
            return redirect("/blog/post/{}/".format(form.post.slug))


class DeleteComment(LoginRequiredMixin, DeleteView):
    """Удаление комментария"""
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def get_queryset(self):
        self.success_url = Post.objects.get(comment=self.kwargs.get('pk')).get_absolute_url()
        return self.model.objects.filter(id=self.kwargs.get('pk'))


class AddUserPost(LoginRequiredMixin, CreateView):
    """Статья предложенная пользователем"""
    model = Post
    form_class = UserPostForm
    template_name = 'blog/add-post-user.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.published = False
        self.success_url = reverse_lazy('blog')
        form.save()
        return super(AddUserPost, self).form_valid(form)
