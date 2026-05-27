from rest_framework import serializers
from polls.tables.instructor import Instructor

class InstructorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Instructor
        fields = "__all__"