from django.db import models
from . import managers


class ClassInfoModel(models.Model):
    DEFAULT = "--선택--"
    MAJOR = "전공"
    ELECTIVES = "교양"
    CLASS_CHOICES = ((MAJOR, "전공"), (ELECTIVES, "교양"))

    CREDIT0 = 0.5
    CREDIT1 = 1
    CREDIT2 = 2
    CREDIT3 = 3
    CREDIT_CHOICES = (
        (CREDIT0, "0.5"),
        (CREDIT1, "1"),
        (CREDIT2, "2"),
        (CREDIT3, "3"),
    )
    GRADE_FIRST = "1"
    GRADE_SECOND = "2"
    GRADE_THIRD = "3"
    GRADE_FOURTH = "4"
    GRADE_FIFTH = "공통"
    GRADE_CHOICES = (
        (GRADE_FIRST, "1"),
        (GRADE_SECOND, "2"),
        (GRADE_THIRD, "3"),
        (GRADE_FOURTH, "4"),
        (GRADE_FIFTH, "공통"),
    )
    UNI_1 = "경영경제대학"
    UNI_2 = "공과대학"
    UNI_3 = "소프트웨어대학"
    UNI_CHOICES = (
        (UNI_1, "경영경제대학"),
        (UNI_2, "공과대학"),
        (UNI_3, "소프트웨어대학"),
    )
    universe = models.CharField(
        ("대학"), choices=UNI_CHOICES, max_length=10, default=DEFAULT
    )
    grade = models.CharField(
        ("학년"), choices=GRADE_CHOICES, max_length=2, default=DEFAULT
    )
    check_major = models.CharField(
        ("이수구분"), choices=CLASS_CHOICES, max_length=10, default=DEFAULT
    )
    subject_number = models.CharField(("과목번호"), max_length=20, blank=True)
    subject_name = models.CharField(("과목명"), max_length=30, blank=True)
    credit = models.CharField(("학점"), max_length=2, blank=True)
    professor = models.CharField(("담당교수"), max_length=5, blank=True)
    time = models.CharField(("강의시간"), max_length=8, blank=True)
    objects = managers.CustomModelManager()

    class Meta:
        abstract = True
