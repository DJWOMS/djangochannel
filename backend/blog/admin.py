from django.contrib import admin
from django.contrib import messages
from backend.blog.models import Post, Tag, SpySearch, BlogCategory, Comment
from mptt.admin import MPTTModelAdmin


class TagAdmin(admin.ModelAdmin):
    """Тэги"""
    prepopulated_fields = {"slug": ("name",)}


class ActionPublish:
    """Action для публикации и снятия с публикации"""

    def unpublish(self, request, queryset):
        """Снять с публикации"""
        rows_updated = queryset.update(published=False)
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)

    unpublish.short_description = "Снять с публикации"
    unpublish.allowed_permissions = ('change',)

    def publish(self, request, queryset):
        """Опубликовать"""
        rows_updated = queryset.update(published=True)
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)

    publish.short_description = "Опубликовать"
    publish.allowed_permissions = ('change',)


class BlogCategoryAdmin(MPTTModelAdmin, ActionPublish):
    """Категории"""
    list_display = ("name", "parent", "slug", "published", "id")
    prepopulated_fields = {"slug": ("name",)}
    mptt_level_indent = 15
    list_filter = ("published",)
    actions = ['unpublish', 'publish']

    # def cat(self, request, queryset):
    #     """Определение категорий """
    #     with open('update_category/mp_cat.py', 'a') as file:
    #         l = []
    #         for cat in queryset:
    #             mp_name = cat.name
    #             mp_id = cat.id
    #             d = {mp_name: mp_id}
    #             l.append(d)
    #         file.write('mp_category_dict = {}\n'.format(l))
    # cat.short_description = "Определить"


class PostAdmin(admin.ModelAdmin, ActionPublish):
    """Статьи"""
    list_display = ('title', 'slug', 'created_date', "category", "published", "id")
    list_filter = ("created_date", "category__name", "published")
    search_fields = ("title", "category")
    prepopulated_fields = {"slug": ("title",)}
    actions = ['unpublish', 'publish']

    # def new_category(self, request, queryset):
    #     """Переопределение категорий постов"""
    #     for post in queryset:
    #         post_id = post.id
    #     for key, value in redefine_categories().items():
    #             if post_id == key:
    #                 queryset.update(category_id=value)
    # new_category.short_description = "Переопределить"


class CommentAdmin(admin.ModelAdmin, ActionPublish):
    """Коментарии к статьям"""
    list_display = ("user", "post", "date", "update", "published")
    actions = ['unpublish', 'publish']


class SpySearchAdmin(admin.ModelAdmin):
    """Счетчик поиска"""
    list_display = ("record", "counter")


# admin.site.add_action(PostAdmin.publish)
# admin.site.add_action(PostAdmin.unpublish)

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(SpySearch, SpySearchAdmin)
admin.site.register(BlogCategory, BlogCategoryAdmin)
