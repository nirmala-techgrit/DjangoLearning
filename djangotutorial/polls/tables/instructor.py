from django.db import models
from .abstract import CommonFields

# Instructor Model
class Instructor(CommonFields):
    full_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name