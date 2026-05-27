from rest_framework import serializers
from polls.tables.student_course import StudentCourse

class StudentCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentCourse
        fields = "__all__"