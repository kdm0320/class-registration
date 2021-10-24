from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from core import managers as core_managers


def default_time_table_dict():
    return {"월": [], "화": [], "수": [], "목": [], "금": []}


class List(models.Model):

    user = models.OneToOneField(
        "users.User", related_name="lists", on_delete=models.CASCADE, null=True
    )
    subjects = models.ManyToManyField("classs.Class", blank=True)
    objects = core_managers.CustomModelManager()
    time_table = models.JSONField(("시간표"), null=True, default=default_time_table_dict)
    credits = models.FloatField(
        ("신청학점"), default=0, validators=[MinValueValidator(0), MaxValueValidator(23)]
    )

    def number(self):
        return self.user