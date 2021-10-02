from os import name
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
        null=True,
        validators=[MaxValueValidator(99999999)],
    )
    major = models.CharField(("전공"), null=True, max_length=15)
    grade = models.CharField(("학년"), choices=GRADE_CHOICES, max_length=2, null=True)
    time_table = models.TextField(("시간표"), null=True, blank=True)