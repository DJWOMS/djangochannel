from django.contrib import admin
from .models import Pay


class PayAdmin(admin.ModelAdmin):
    """Платежи"""
    list_display = ("item", "account", "status", "id")

admin.site.register(Pay, PayAdmin)
