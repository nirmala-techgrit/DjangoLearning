from django.db import models
from .abstract import CommonFields
from .instructor import Instructor

# Course Model
class Course(CommonFields):
    name = models.CharField(max_length=255)
    duration = models.CharField(max_length=100)

    instructor = models.ForeignKey(
        Instructor,
        on_delete=models.CASCADE,
        related_name='courses'
    )

    def __str__(self):
        return self.name