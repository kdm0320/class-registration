from django.contrib import admin
from . import models


@admin.register(models.registration)
class RegiAdmin(admin.ModelAdmin):
    pass
