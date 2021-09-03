from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)  # decorator
class CustomUserAdmin(UserAdmin):
    """Custom User Admin"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Personal information",
            {
                "fields": (
                    "number",
                    "major",
                    "grade",
                    "basket_subjects",
                    "registed_subjects",
                    "time_table",
                )
            },
        ),
    )
    list_display = (
        "username",
        "number",
        "major",
        "grade",
        "email",
        "get_baskets",
    )
    list_filter = ("major", "grade")

    filter_horizontal = ("basket_subjects",)