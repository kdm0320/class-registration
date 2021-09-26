from django.db import models


class List(models.Model):

    user = models.OneToOneField(
        "users.User", related_name="lists", on_delete=models.CASCADE
    )
    subjects = models.ManyToManyField("classs.Class", blank=True)

    def number(self):
        return self.user