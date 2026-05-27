from rest_framework import serializers
from polls.tables.course import Course

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"