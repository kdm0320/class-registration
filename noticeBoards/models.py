from django.db import models


class notice(models.Model):
    """Notice Model Definition"""

    number = models.PositiveIntegerField()
    title = models.CharField(max_length=50)
    content = models.TextField(("내용을 입력하세요"))
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
