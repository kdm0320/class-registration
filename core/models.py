from django.db import models
from django.db.models.expressions import F
from django.db.models.fields import BooleanField, CharField


class ClassInfoModel(models.Model):
    """ClassInfoModel Definition"""

    MAJOR = "majaor"
    ELECTIVES = "electives"
    CLASS_CHOICES = ((MAJOR, "전공"), (ELECTIVES, "교양"))

    CREDIT1 = "1"
    CREDIT2 = "2"
    CREDIT3 = "3"
    CREDIT_CHOICES = (
        (CREDIT1, "1"),
        (CREDIT2, "2"),
        (CREDIT3, "3"),
    )
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
    grade = models.CharField(choices=GRADE_CHOICES, max_length=2)
    check_major = CharField(choices=CLASS_CHOICES, max_length=10, default="--선택--")
    subject_number = CharField(max_length=20, blank=True)
    subject_name = CharField(max_length=30, blank=True)
    credit = CharField(choices=CREDIT_CHOICES, max_length=2, blank=True)
    professor = CharField(max_length=5, blank=True)
    is_closed = BooleanField(default=False)

    class Meta:
        abstract = True  # 데이터베이스에 등록 안됨
