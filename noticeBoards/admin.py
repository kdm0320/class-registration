from django.contrib import admin
from . import models


@admin.register(models.notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = (
        "type",
        "title",
        "department",
        "writer",
        "created",
        "post_hit",
    )
