from django.contrib import admin
from . import models


@admin.register(models.notice)
class NoticeAdmin(admin.ModelAdmin):
    pass
