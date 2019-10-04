from django.contrib import admin
from .models import Review


class ReviewsAdmin(admin.ModelAdmin):
    """Отзывы пользователей"""
    list_display = ("name", "user", "moderated")
    list_editable = ("moderated",)

admin.site.register(Review, ReviewsAdmin)
