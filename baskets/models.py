from django.db import models
from core import models as core_models


class basket(core_models.ClassInfoModel):
    """Basket Model Definition"""

    available = models.PositiveIntegerField(("수강 가능 인원수"), default=0)
    left = models.PositiveIntegerField(("여석"), default=0)

    def __str__(self):
        return self.subject_name
