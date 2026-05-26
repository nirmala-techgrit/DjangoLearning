from django.db import models
from .abstract import CommonFields
from .course import Course
from .student import Student

# Review Model
class Review(CommonFields):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    content = models.TextField()

    def __str__(self):
        return f"Review by {self.student.full_name}"