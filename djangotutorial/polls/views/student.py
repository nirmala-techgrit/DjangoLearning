from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from polls.tables.student import Student
from polls.serializers.student import StudentSerializer


# CREATE + LIST
class StudentListCreateAPIView(APIView):

    # Get All Students
    def get(self, request):

        students = Student.objects.all()

        serializer = StudentSerializer(
            students,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    # Create Student
    def post(self, request):

        serializer = StudentSerializer(
            data=request.data
        )

        if serializer.is_valid(raise_exception=True):

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


# RETRIEVE + UPDATE + DELETE
class StudentDetailAPIView(APIView):

    def get_object(self, pk):

        try:
            return Student.objects.get(pk=pk)

        except Student.DoesNotExist:
            return None

    # Get Single Student
    def get(self, request, pk):

        student = self.get_object(pk)

        if not student:
            return Response(
                {"error": "Student not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = StudentSerializer(student)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    # Update Student
    def put(self, request, pk):

        student = self.get_object(pk)

        if not student:
            return Response(
                {"error": "Student not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = StudentSerializer(
            student,
            data=request.data
        )

        if serializer.is_valid(raise_exception=True):

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    # Delete Student
    def delete(self, request, pk):

        student = self.get_object(pk)

        if not student:
            return Response(
                {"error": "Student not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        student.delete()

        return Response(
            {"message": "Student deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )


class StudentAPIUsingGenericAPIView(GenericAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = "pk"

    def get_object(self, pk):

        try:
            return Student.objects.get(pk=pk)

        except Student.DoesNotExist:
            return None

    # GET -> List + Retrieve
    def get(self, request, pk=None):

        # Get Single Student
        if pk:

            student = self.get_object(pk)

            if not student:

                return Response(
                    {"error": "Student not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

            serializer = self.get_serializer(student)

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        # Get All Students
        students = self.get_queryset()

        serializer = self.get_serializer(
            students,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    # POST -> Create Student
    def post(self, request):

        serializer = self.get_serializer(
            data=request.data
        )

        if serializer.is_valid(raise_exception=True):

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    # PUT -> Update Student
    def put(self, request, pk):

        student = self.get_object(pk)

        if not student:

            return Response(
                {"error": "Student not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(
            student,
            data=request.data
        )

        if serializer.is_valid(raise_exception=True):

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    # DELETE -> Delete Student
    def delete(self, request, pk):

        student = self.get_object(pk)

        if not student:

            return Response(
                {"error": "Student not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        student.delete()

        return Response(
            {"message": "Student deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )