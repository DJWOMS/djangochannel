from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from django.contrib import messages
from backend.blog.models import Post, Tag, SpySearch, BlogCategory, Comment
from mptt.admin import MPTTModelAdmin


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


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Тэги"""
    prepopulated_fields = {"slug": ("name",)}


@admin.register(BlogCategory)
class BlogCategoryAdmin(MPTTModelAdmin, ActionPublish):
    """Категории"""
    list_display = ("name", "parent", "slug", "published", "id")
    prepopulated_fields = {"slug": ("name",)}
    mptt_level_indent = 15
    list_filter = ("published",)
    actions = ['unpublish', 'publish']


class PostAdminForm(forms.ModelForm):
    """Виджет редактора ckeditor"""
    mini_text = forms.CharField(label="Превью статьи", widget=CKEditorUploadingWidget())
    text = forms.CharField(label="Полная статья", widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin, ActionPublish):
    """Статьи"""
    list_display = ('title', 'slug', 'created_date', "published_date", "category", "published", "id")
    list_filter = ("created_date", "category__name", "published")
    search_fields = ("title", "category")
    prepopulated_fields = {"slug": ("title",)}
    actions = ['unpublish', 'publish']
    form = PostAdminForm
    save_on_top = True
    save_as = True


@admin.register(Comment)
class CommentAdmin(MPTTModelAdmin, ActionPublish):
    """Коментарии к статьям"""
    list_display = ("user", "post", "created_date", "update_date", "published", "id")
    actions = ['unpublish', 'publish']
    mptt_level_indent = 15


@admin.register(SpySearch)
class SpySearchAdmin(admin.ModelAdmin):
    """Счетчик поиска"""
    list_display = ("record", "counter")


# admin.site.add_action(PostAdmin.publish)
# admin.site.add_action(PostAdmin.unpublish)
