from django.contrib import admin
from . import models


@admin.register(models.Clas)
class ClassAdmin(admin.ModelAdmin):
    pass
