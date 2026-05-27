from rest_framework import viewsets
from polls.tables.instructor import Instructor
from polls.serializers.instructor import InstructorSerializer

class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer