from django.db import models
from .abstract import CommonFields

# Student Model
class Student(CommonFields):
    full_name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name