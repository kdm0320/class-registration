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
    )
    list_filter = ("major", "grade")