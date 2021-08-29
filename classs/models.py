from django.db import models
from core import models as core_models


class Class(core_models.ClassInfoModel):
    """Class Model Definition"""

    DEP_1 = "경제학과"
    DEP_2 = "전자공학과"
    DEP_3 = "소프트웨어학과"
    DEP_CHOICES = (
        (DEP_1, "경제학과"),
        (DEP_2, "전자공학과"),
        (DEP_3, "소프트웨어학과"),
    )
    department = models.CharField(
        ("개설학과"), choices=DEP_CHOICES, max_length=20, default="--선택--"
    )

    def __str__(self):
        return self.subject_name
