from django.db import models


class ClassInfoModel(models.Model):
    MAJOR = "전공"
    ELECTIVES = "교양"
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
    GRADE_FIFTH = "공통"
    GRADE_CHOICES = (
        (GRADE_FIRST, "1"),
        (GRADE_SECOND, "2"),
        (GRADE_THIRD, "3"),
        (GRADE_FOURTH, "4"),
        (GRADE_FIFTH, "공통"),
    )
    grade = models.CharField(
        ("학년"), choices=GRADE_CHOICES, max_length=2, default="--선택--"
    )
    check_major = models.CharField(
        ("이수구분"), choices=CLASS_CHOICES, max_length=10, default="--선택--"
    )
    subject_number = models.CharField(("과목번호"), max_length=20, blank=True)
    subject_name = models.CharField(("과목명"), max_length=30, blank=True)
    credit = models.CharField(("학점"), choices=CREDIT_CHOICES, max_length=2, blank=True)
    professor = models.CharField(("담당교수"), max_length=5, blank=True)
    is_closed = models.BooleanField(("폐강"), default=False)

    class Meta:
        abstract = True
