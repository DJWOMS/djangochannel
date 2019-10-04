from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import CategoryTask, DCTask, AnswerDCTask, Skills


class CategoryTaskAdmin(MPTTModelAdmin):
    """Категории заданий"""
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "id")
    mptt_level_indent = 20


class DCTaskAdmin(admin.ModelAdmin):
    """Задания"""
    list_display = ("title", "category", "mastery", "id")
    prepopulated_fields = {"slug": ("title",)}


class AnswerDCTaskAdmin(admin.ModelAdmin):
    """Взятые задания"""
    list_display = ("id", "user", "task", "created", "result", "check")
    list_display_links = ("user",)


class SkillsAdmin(admin.ModelAdmin):
    """Навыки пользователя"""
    list_display = ("user", "skill", "points")


admin.site.register(CategoryTask, CategoryTaskAdmin)
admin.site.register(DCTask, DCTaskAdmin)
admin.site.register(AnswerDCTask, AnswerDCTaskAdmin)

admin.site.register(Skills, SkillsAdmin)