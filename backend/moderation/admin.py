from django.contrib import admin

from .models import SimpleRight, ModeratorRights, BannedUser

admin.site.register(SimpleRight)
admin.site.register(ModeratorRights)
admin.site.register(BannedUser)
