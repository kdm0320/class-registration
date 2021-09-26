from django.db import models
from core import models as core_models


class Class(core_models.ClassInfoModel):
    """Class Model Definition"""

    department = models.CharField(("개설학과"), max_length=20, default="--선택--", blank=True)
    people = models.PositiveIntegerField(verbose_name="수강 가능인원", default=0)

    def __str__(self):
        return self.subject_name