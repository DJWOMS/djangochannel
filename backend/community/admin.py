from django.contrib import admin

from .models import Groups, EntryGroup, GroupLink, CommentEntryGroup


@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    """Группы и команды"""

    list_display = ("title", "founder", "group_variety", "id")
    search_fields = ("title",)


@admin.register(EntryGroup)
class EntryGroupAdmin(admin.ModelAdmin):
    """Записи группы"""

    list_display = ("title", "group", "author", "id")
    search_fields = ("title",)


@admin.register(GroupLink)
class GroupLinkAdmin(admin.ModelAdmin):
    """Ссылки группы"""

    list_display = ("title", "link", "id")
    search_fields = ("title",)


@admin.register(CommentEntryGroup)
class CommentEntryGroupAdmin(admin.ModelAdmin):
    """Комментарии к записям в группе"""

    list_display = ("author", "entry", "id")
    search_fields = ("author", "entry")
