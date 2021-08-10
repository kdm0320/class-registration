from django.db import models
from django.db.models.fields import TextField
from core import models as core_models


class registration(core_models.ClassInfoModel):
    """Registration Model Definition"""

    class_list = TextField()
