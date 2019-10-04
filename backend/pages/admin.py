from django.contrib import admin

from .models import Pages


@admin.register(Pages)
class PagesAdmin(admin.ModelAdmin):
    """Статичные страницы"""
    list_display = ("title", "published", "id")
    list_editable = ("published",)
    list_filter = ("published", "template")
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title", )}