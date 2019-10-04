from django.contrib import admin
from .models import PersonalRecords, UserProfile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "count_course", "id")


@admin.register(PersonalRecords)
class PersonalRecordsAdmin(admin.ModelAdmin):
    """Дневник пользователя"""
    list_display = ("user", "title", "for_all", "date", "update")
    search_fields = ("user",)


admin.site.register(UserProfile, ProfileAdmin)
