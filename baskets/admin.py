from django.contrib import admin
from . import models


@admin.register(models.basket)
class BasketAdmin(admin.ModelAdmin):
    pass
