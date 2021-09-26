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
                    "people",
                )
            },
        ),
    )

    list_display = (
        "subject_name",
        "grade",
        "check_major",
        "subject_number",
        "credit",
        "professor",
        "time",
        "universe",
        "department",
        "people",
    )
