from django.db import models
from core import managers as core_managers


class List(models.Model):

    user = models.OneToOneField(
        "users.User", related_name="lists", on_delete=models.CASCADE, null=True
    )
    subjects = models.ManyToManyField("classs.Class", blank=True)
    objects = core_managers.CustomModelManager()
    time_table = models.JSONField(
        ("시간표"), null=True, default=dict(월=[], 화=[], 수=[], 목=[], 금=[])
    )

    def number(self):
        return self.user
