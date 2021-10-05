from django.contrib import admin
from . import models


@admin.register(models.List)
class ClassAdmin(admin.ModelAdmin):
    list_display = ("user",)
    filter_horizontal = ("subjects",)
