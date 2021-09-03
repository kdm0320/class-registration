from django.contrib import admin
from . import models
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin


@admin.register(models.Class)
class ClassAdmin(ImportExportMixin, admin.ModelAdmin):
    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "grade",
                    "check_major",
                    "subject_number",
                    "subject_name",
                    "credit",
                    "professor",
                    "time",
                    "universe",
                    "department",
                )
            },
        ),
    )

    list_display = (
        "grade",
        "check_major",
        "subject_number",
        "subject_name",
        "credit",
        "professor",
        "time",
        "universe",
        "department",
    )