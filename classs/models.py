from django.db import models
from django.db.models.fields import CharField
from core import models as core_models


class Class(core_models.ClassInfoModel):
    """Class Model Definition"""

    department = CharField(max_length=20)
