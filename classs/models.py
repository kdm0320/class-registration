from django.db import models
from django.db.models.fields import CharField
from core import models as core_models


class Class(core_models.ClassInfoModel):
    """Class Model Definition"""

    department = CharField(max_length=20)

    def __str__(self):
        return self.subject_name


class basket(Class):
    """Basket Model Definition"""

    available = models.PositiveIntegerField(default=0)
    left = models.PositiveIntegerField(default=0)


class registration(Class):
    """Registration Model Definition"""

    regi_list = models.TextField(("수강신청 과목 리스트"))
