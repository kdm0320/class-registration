from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# class IntegerRangeField(models.IntegerField):
#     def __init__(
#         self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs
#     ):
#         self.min_value, self.max_value = min_value, max_value
#         models.IntegerField.__init__(self, verbose_name, name, **kwargs)

#     def formfield(self, **kwargs):
#         defaults = {"min_value": self.min_value, "max_value": self.max_value}
#         defaults.update(kwargs)
#         return super(IntegerRangeField, self).formfield(**defaults)


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
