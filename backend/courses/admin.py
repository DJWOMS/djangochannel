from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import (Category,
                     Course,
                     Task,
                     RealizationTask,
                     MessageForStudent,
                     MessagesTask,
                     CheckPAyUser)
from backend.utils.admin import all_fields


class CategoryAdmin(admin.ModelAdmin):
    """Админка категорий"""
    list_display = ('title',)


class CourseAdmin(admin.ModelAdmin):
    """Админка курсов"""
    list_display = (
        "id", "title", "category", "price", "date_start", "available", "is_active", "is_complete"
    )
    list_filter = ("title", "category", "is_active", "is_complete")
    # list_display.append('term')
    # list_display.append('count_seats')
    readonly_fields = ('count_tasks',)
    list_display_links = ("title",)
    prepopulated_fields = {"slug": ("title",)}
    actions = ['complete_the_course']

    def complete_the_course(self, request, queryset):
        """Переводит курс в статус False, удаляет студентов"""
        queryset.update(is_active=False)
        for course in queryset:
            for user in course.students.all():
                user.profile.completed_courses.add(course)
                course.students.remove(user)
    complete_the_course.short_description = "Завершить курс"


class TaskAdmin(admin.ModelAdmin):
    """Админка заданий"""
    list_display = all_fields(Task, 'id', 'description')
    list_display_links = ("title",)
    actions = ['show_task']

    def show_task(self, request, queryset):
        """Переводит курс в статус False, удаляет студентов"""
        queryset.update(active=True)
    show_task.short_description = "Вывести задание"


class RealizationTaskAdmin(admin.ModelAdmin):
    """Админка выполнения заданий"""

    class MessagesTaskAdmin(admin.TabularInline):
        """
        Возможность добавления вопросов
        сразу при создании теста
        """
        model = MessagesTask

    inlines = [
        MessagesTaskAdmin,
    ]

    list_display = ("id", "student", "task", "success", "date_create")
    list_filter = ("task__title", "student__username", "date_create")
    list_editable = ("success",)
    readonly_fields = ('answer',)
    list_display_links = ("student",)
    # fields = ["task", "student", "answer", "comment", "success"]

    def answer(self, obj):
        return mark_safe("{}|safe".format(obj.answer))


class MessagesTaskAdmin(admin.ModelAdmin):
    """Сообщения в задании"""
    list_display = ("user", "realiz_task", "created")


class MessForStudentAdmin(admin.ModelAdmin):
    """Отправка сообщений студентам курса"""
    list_display = ("subject", "course", "date")


class CheckPAyUserAdmin(admin.ModelAdmin):
    """Ожидание оплаты"""
    list_display = ("user", "course", "date", "status")


admin.site.register(MessageForStudent, MessForStudentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(RealizationTask, RealizationTaskAdmin)
admin.site.register(MessagesTask, MessagesTaskAdmin)
admin.site.register(CheckPAyUser, CheckPAyUserAdmin)
