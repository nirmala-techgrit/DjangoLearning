from django.contrib import admin
from polls.tables.course import Course
from polls.tables.instructor import Instructor
from polls.tables.student import Student
from polls.tables.reviews import Review
from polls.tables.student_course import StudentCourse

# Register your models here.

admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Student)
admin.site.register(Review)
admin.site.register(StudentCourse)
