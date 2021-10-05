from django.db import models
from django.urls import reverse


class notice(models.Model):
    """Notice Model Definition"""

    TYPE_FIRST = "공지"
    TYPE_SECOND = "문의"
    TYPE_CHOCIES = (
        (TYPE_FIRST, "공지"),
        (TYPE_SECOND, "문의"),
    )
    title = models.CharField(("제목"), max_length=50)
    type = models.CharField(
        ("종류"), choices=TYPE_CHOCIES, max_length=10, default="--선택--"
    )
    content = models.TextField(("내용"), default="")
    department = models.CharField(("소속"), max_length=10, default="")
    writer = models.CharField(
        ("작성자"),
        max_length=20,
        default="",
    )
    created = models.DateField(("작성일"), auto_now_add=True)
    updated = models.DateField(auto_now=True)
    post_hit = models.PositiveIntegerField(("조회수"), default=0)

    def __str__(self):
        return self.title

    def update_count(self):
        self.post_hit += 1
        self.save()

    def get_absolute_url(self):
        return reverse("notices:detail", kwargs={"pk": self.pk})
