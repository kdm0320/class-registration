from django.contrib import admin
from . import models


@admin.register(models.Class)
class ClassAdmin(admin.ModelAdmin):
    pass


@admin.register(models.basket)
class BasketAdmin(admin.ModelAdmin):
    pass
