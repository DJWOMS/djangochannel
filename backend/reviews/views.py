from django.conf import settings
from django.contrib import messages
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Review
from .forms import ReviewsForm


class ListReviews(ListView):
    """Вывод всех отзывов"""
    queryset = Review.objects.filter(moderated=True)
    template_name = "reviews/list.html"
    paginate_by = 8


class AddReview(LoginRequiredMixin, CreateView):
    """Добавление одзыва"""
    model = Review
    form_class = ReviewsForm
    template_name = "reviews/add.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        messages.add_message(self.request, settings.MY_INFO,
                         'Спасибо, Ваш отзыв отправлен и в ближайшее время будет опубликован')
        return super(AddReview, self).form_valid(form)
