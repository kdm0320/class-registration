from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class User(AbstractUser):
    """Custom User Model"""

    GRADE_FIRST = "1"
    GRADE_SECOND = "2"
    GRADE_THIRD = "3"
    GRADE_FOURTH = "4"

    GRADE_CHOICES = (
        (GRADE_FIRST, "1"),
        (GRADE_SECOND, "2"),
        (GRADE_THIRD, "3"),
        (GRADE_FOURTH, "4"),
    )
    number = models.PositiveIntegerField(
        ("학번"),
        default=20140000,
        validators=[MinValueValidator(20140000), MaxValueValidator(99999999)],
    )
    major = models.CharField(("전공"), null=True, max_length=15)
    grade = models.CharField(("학년"), choices=GRADE_CHOICES, max_length=2, null=True)
    basket_subjects = models.ManyToManyField("classs.Class", verbose_name=("장바구니 과목들"))
    registed_subjects = models.ManyToManyField("users.User", verbose_name=("수강신청 과목들"))
    time_table = models.TextField(("시간표"), null=True, blank=True)
