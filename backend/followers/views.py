from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Followers
from .forms import FollowersForm


class AllFriends(LoginRequiredMixin, ListView):
    """Список всех друзей"""
    model = Followers
    template_name = 'followers/friends.html'

    def get_queryset(self):
        return self.model.objects.filter(
            Q(subscribed=self.request.user) |
            Q(friends=self.request.user)).filter(in_friends=True)


class AllFollowers(LoginRequiredMixin, ListView):
    """Список всех подписчиков"""
    model = Followers
    template_name = 'followers/followers-list.html'

    def get_queryset(self):
        return self.model.objects.filter(subscribed=self.request.user).filter(in_followers=True)


class AddFollow(LoginRequiredMixin, CreateView):
    """Подпись на пользователя"""
    model = Followers
    template_name = 'followers/add-request-friends.html'
    form_class = FollowersForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.friends = self.request.user
        form.instance.subscribed = User.objects.get(id=self.kwargs.get("pk"))
        form.save()
        return super(AddFollow, self).form_valid(form)


class FriendRequests(LoginRequiredMixin, ListView):
    """Вывод заявок в друзья"""
    model = Followers
    template_name = 'followers/requests-follow.html'

    def get_queryset(self):
        return Followers.objects.filter(subscribed=self.request.user).filter(Q(in_followers=False) &
                                                                             Q(in_friends=False))


class AddFriends(LoginRequiredMixin, UpdateView):
    """Подтверждение дружбы"""
    model = Followers
    template_name = 'followers/add-request-friends.html'
    form_class = FollowersForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.in_friends = True
        form.instance.in_followers = False
        form.save()
        return super(AddFriends, self).form_valid(form)


class FriendConfirm(LoginRequiredMixin, UpdateView):
    """Подтверждение дружбы через публичный профиль"""
    model = Followers
    template_name = 'followers/add-request-friends.html'
    form_class = FollowersForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        follower = Followers.objects.filter(id=self.kwargs.get("pk"))
        if follower:
            form.instance.in_friends = True
            form.instance.in_followers = False
            form.save()
        return super().form_valid(form)


class NotAddFriends(LoginRequiredMixin, UpdateView):
    """Оставить в подписчиках"""
    model = Followers
    template_name = 'followers/add-request-friends.html'
    form_class = FollowersForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.in_friends = False
        form.instance.in_followers = True
        form.save()
        return super(NotAddFriends, self).form_valid(form)


class RemoveFriends(LoginRequiredMixin, DeleteView):
    """Убрать из друзей, отмена заявки"""
    model = Followers
    template_name = 'followers/delete-friends.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        friend = self.model.objects.filter(Q(subscribed_id=self.kwargs.get('pk')) |
                                           Q(friends_id=self.kwargs.get('pk'))). \
            filter(Q(subscribed_id=self.request.user) | Q(friends_id=self.request.user))
        if friend:
            for dell in friend:
                return dell
        petition = self.model.objects.filter(subscribed_id=self.kwargs.get('pk'), friends_id=self.request.user)
        if petition and petition.in_friends == False and petition.in_followers == False:
            for dell in petition:
                return dell
