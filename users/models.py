from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator


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
        default=0, validators=[MaxValueValidator(99999999)]
    )
    major = models.CharField(null=True, max_length=15)
    grade = models.CharField(choices=GRADE_CHOICES, max_length=2, null=True)
    basket_subjects = models.TextField(null=True)
    registed_subjects = models.TextField(null=True)
    time_table = models.TextField(null=True)
