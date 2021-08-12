from django.db import models
from core import models as core_models


class registration(core_models.ClassInfoModel):
    """Registration Model Definition"""

    regi_list = models.TextField(("수강신청 과목 리스트"))

    def __str__(self):
        return self.subject_name
