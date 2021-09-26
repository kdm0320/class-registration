from django.db import models
from core import managers as core_managers


class List(models.Model):

    user = models.OneToOneField(
        "users.User", related_name="lists", on_delete=models.CASCADE
    )
    subjects = models.ManyToManyField("classs.Class", blank=True)
    objects = core_managers.CustomModelManager()

    def number(self):
        return self.user
