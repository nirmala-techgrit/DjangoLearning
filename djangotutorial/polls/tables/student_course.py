from django.db import models
from .abstract import CommonFields
from .course import Course
from .student import Student

# Student Course Model (Many-to-Many with extra fields)
class StudentCourse(CommonFields):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='student_courses'
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='student_courses'
    )

    score = models.CharField(max_length=50)

    enrollment_date = models.DateField()

    def __str__(self):
        return f"{self.student.full_name} - {self.course.name}"