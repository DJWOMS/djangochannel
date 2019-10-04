import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, DetailView, UpdateView, ListView, CreateView, DeleteView, FormView

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from DS import settings
from backend.message.models import PrivatMessages, Room
from backend.message.forms import MessageForm, RoomForm

from .models import UserProfile, PersonalRecords
from .forms import ProfileForm, PersonalRecordsForm


class ProfileView(LoginRequiredMixin, DetailView):
    """Вывод профиля пользователя"""
    model = UserProfile
    context_object_name = 'profile'
    template_name = 'profile/profile-detail.html'

    def get_object(self, queryset=None):
        obj = get_object_or_404(UserProfile, user=self.request.user)
        if obj.user != self.request.user:
            raise Http404
        return obj


class ProfileEditView(LoginRequiredMixin, UpdateView):
    """Редактирование профиля"""
    form_class = ProfileForm
    model = UserProfile
    context_object_name = 'profile'
    template_name = 'profile/profile-edit.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user.profile

    def form_valid(self, form):
        messages.success(self.request, 'Profile has been updated!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, settings.MY_INFO,
                             'Error')
        return super().form_invalid(form)


class PasswordChangeView(LoginRequiredMixin, FormView):
    """Смена пароля пользователем"""
    model = User
    form_class = PasswordChangeForm
    template_name = 'profile/password-edit.html'
    success_url = reverse_lazy('password_edit')

    def get_form_kwargs(self):
        kwargs = super(PasswordChangeView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        if self.request.method == 'POST':
            kwargs['data'] = self.request.POST
        return kwargs

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Пароль изменен успешно')
        update_session_auth_hash(self.request, form.user)
        return super(PasswordChangeView, self).form_valid(form)


class AllUserProfile(LoginRequiredMixin, ListView):
    """Вывод всех публичных пропрофилей пользователей"""
    model = UserProfile
    template_name = 'profile/all-user-profile.html'
    success_url = reverse_lazy('profile')

    def get_queryset(self):
        return self.model.objects.filter(public=True).exclude(user_id=self.request.user)


class PublicUserInfo(LoginRequiredMixin, DetailView):
    """Публичный профиль пользователя"""
    model = UserProfile
    context_object_name = 'profile'
    template_name = 'profile/public-user-info.html'

    def get_object(self, queryset=None):
        obj = get_object_or_404(UserProfile, user=self.kwargs.get('pk'))
        return obj

    # def get_queryset(self):
    #     profile = self.get_object()
    #     user = User.objects.get(id=profile.id)
    #     qs = user.twits.all()
    #     return qs
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['posts'] = self.get_queryset()
    #     return context


class MessagesList(LoginRequiredMixin, ListView):
    """Список сообщений"""
    template_name = "profile/list-mess.html"

    def get_queryset(self):
        return Room.objects.filter(Q(creator=self.request.user) | Q(recipient=self.request.user))


class Rooms(LoginRequiredMixin, View):
    """Создание комнаты чата"""

    def get(self, request):
        context = {
            "form_room": RoomForm(),
            "form_mess": MessageForm()
        }
        return render(request, 'profile/create-mess.html', context)

    def post(self, request):
        print(request.POST)
        form_room = RoomForm(request.POST)
        form_mess = MessageForm(request.POST)
        if form_room.is_valid() and form_mess.is_valid():
            form_room = form_room.save(commit=False)
            form_room.creator = request.user
            form_room.save()
            form_mess = form_mess.save(commit=False)
            form_mess.user = request.user
            form_mess.room_id = form_room.id
            form_mess.save()
        return redirect('detail_message', pk=form_room.id)


class DetailMessages(LoginRequiredMixin, View):
    """Полное сообщение"""

    def mess_read(self, id, user):
        mess = PrivatMessages.objects.filter(room_id=id, read=False).exclude(user=user)
        for message in mess:
            message.read = True
            message.save()

    def get(self, request, **kwargs):
        context = {"form": MessageForm()}
        context["messages"] = PrivatMessages.objects.filter(room=kwargs.get('pk')) \
            .filter(Q(room__creator=request.user) | Q(room__recipient=request.user))
        self.mess_read(id=kwargs.get('pk'), user=request.user)
        return render(request, "profile/detail-mess.html", context)

    def post(self, request, **kwargs):
        form = MessageForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.room_id = kwargs.get('pk')
            form.save()
        return HttpResponseRedirect(request.path)


class PersonalRecordsList(LoginRequiredMixin, ListView):
    """Вывод всех записей дневника пользователя"""
    model = PersonalRecords
    template_name = 'profile/personal-records.html'

    def get_queryset(self):
        return self.model.objects.filter(user_id=self.kwargs.get("pk"))


class PersonalRecordsDetail(LoginRequiredMixin, DetailView):
    """Вывод конкретной записи дневника"""
    model = PersonalRecords
    context_object_name = 'diary'
    template_name = 'profile/personal-records-detail.html'


class PersonalRecordsCreate(LoginRequiredMixin, CreateView):
    """Добавление записей в дневник"""
    model = PersonalRecords
    form_class = PersonalRecordsForm
    template_name = 'profile/add-records.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        self.success_url = reverse_lazy('personal_records', kwargs={"pk": self.request.user.id})
        form.save()
        return super(PersonalRecordsCreate, self).form_valid(form)


class PersonalRecordsUpdate(LoginRequiredMixin, UpdateView):
    """Редактирование записи дневника"""
    model = PersonalRecords
    form_class = PersonalRecordsForm
    template_name = 'profile/add-records.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        self.success_url = reverse_lazy('detail_record', kwargs={"pk": self.kwargs.get("pk")})
        form.instance.update = datetime.datetime.now()
        form.save()
        return super(PersonalRecordsUpdate, self).form_valid(form)


class PersonalRecordsDelete(LoginRequiredMixin, DeleteView):
    """Удаление записи"""
    model = PersonalRecords
    template_name = 'profile/personal-records-delete.html'

    def get_queryset(self):
        self.success_url = reverse_lazy('personal_records', kwargs={"pk": self.request.user.id})
        return self.model.objects.filter(id=self.kwargs.get('pk'))


class SortedPersonalRecords(LoginRequiredMixin, ListView):
    """Фильтр записей дневника"""
    model = PersonalRecords
    template_name = 'profile/personal-records.html'

    def get_queryset(self):
        if self.request.GET.get('all'):
            sorts = self.model.objects.filter(user_id=self.request.user)
        elif self.request.GET.get('update'):
            sorts = self.model.objects.filter(update__lte=self.request.GET.get('update'), user_id=self.request.user)
        elif self.request.GET.get('pbl'):
            sorts = self.model.objects.filter(for_all=self.request.GET.get('pbl'), user_id=self.request.user)
        else:
            sorts = self.model.objects.filter(for_all=self.request.GET.get('public'), user_id=self.request.user)
        return sorts


class SearchUser(LoginRequiredMixin, ListView):
    """Поиск пользователей по нику"""
    paginate_by = 5
    template_name = "profile/all-user-profile.html"

    def get_queryset(self):
        return UserProfile.objects.filter(name__icontains=self.request.GET.get('qus'))


class AllRecordsOfUsers(LoginRequiredMixin, ListView):
    """Вывод всех публичных записей дневников"""
    model = PersonalRecords
    context_object_name = 'diary'
    template_name = 'profile/all-records-of-users.html'

    def get_queryset(self):
        return self.model.objects.filter(for_all=True)
