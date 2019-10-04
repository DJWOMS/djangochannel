from django.contrib import admin

from .models import Category, Section, Topic, Message
from backend.utils.admin import all_fields


class CategoryAdmin(admin.ModelAdmin):
    """Админка категорий"""
    list_display = ('title', 'id')


class SectionAdmin(admin.ModelAdmin):
    """Админка разделов"""
    list_display = ("id", "title", "category", "created", 'modified')
    list_display_links = ("title", )
    prepopulated_fields = {"slug": ("title",)}


class TopicAdmin(admin.ModelAdmin):
    """Админка тем"""
    list_display = ("id", "title", "user", "modified", 'moderated', 'deleted', 'private', "created")
    list_display_links = ("title", )
    list_editable = ('moderated', 'deleted', 'private')


class MessageAdmin(admin.ModelAdmin):
    """Админка сообщений"""
    list_display = ("id", "user", "topic", 'moderated', 'deleted', "created")
    list_display_links = ("user", )


# class TopicAdmin(admin.ModelAdmin):
#     """Админка топиков"""
#     list_display = all_fields(Topic)
#     list_editable = ('moderated', 'deleted', 'private')


admin.site.register(Category)
admin.site.register(Section, SectionAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Message, MessageAdmin)
