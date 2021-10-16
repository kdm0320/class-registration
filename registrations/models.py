from django.db import models
from core import managers as core_managers


def default_time_table_dict():
    return {"월": [], "화": [], "수": [], "목": [], "금": []}


class registration(models.Model):

    user = models.OneToOneField(
        "users.User", related_name="resgistration", on_delete=models.CASCADE, null=True
    )
    subjects = models.ManyToManyField("classs.Class", blank=True)
    time_table = models.JSONField(("시간표"), null=True, default=default_time_table_dict)
    objects = core_managers.CustomModelManager()

    def number(self):
        return self.user
