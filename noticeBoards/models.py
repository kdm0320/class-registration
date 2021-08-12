from django.db import models


class notice(models.Model):
    """Notice Model Definition"""

    number = models.PositiveIntegerField()
    title = models.CharField(max_length=50)
    content = models.TextField(("내용을 입력하세요"))
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
