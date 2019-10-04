from django.contrib import admin
from .models import Followers


@admin.register(Followers)
class FollowersAdmin(admin.ModelAdmin):
    """Друзья пользователя"""
    list_display = ("subscribed", "friends", "in_friends", "in_followers", "id")
    search_fields = ("subscribed",)
    list_editable = ("in_friends", "in_followers")
