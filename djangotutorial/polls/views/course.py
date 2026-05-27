from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from polls.tables.course import Course
from polls.serializers.course import CourseSerializer


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def course_details(request, pk=None):

    # GET -> List + Retrieve
    if request.method == 'GET':

        # Get Single Course
        if pk:

            try:
                course = Course.objects.get(pk=pk)

            except Course.DoesNotExist:

                return Response(
                    {"error": "Course not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

            serializer = CourseSerializer(course)

            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )

        # Get All Courses
        courses = Course.objects.all()

        serializer = CourseSerializer(
            courses,
            many=True
        )

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    # POST -> Create Course
    elif request.method == 'POST':

        serializer = CourseSerializer(
            data=request.data
        )

        if serializer.is_valid(raise_exception=True):

            serializer.save()

            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    # PUT -> Update Course
    elif request.method == 'PUT':

        try:
            course = Course.objects.get(pk=pk)

        except Course.DoesNotExist:

            return Response(
                {"error": "Course not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CourseSerializer(
            course,
            data=request.data
        )

        if serializer.is_valid(raise_exception=True):

            serializer.save()

            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    # DELETE -> Delete Course
    elif request.method == 'DELETE':

        try:
            course = Course.objects.get(pk=pk)

        except Course.DoesNotExist:

            return Response(
                {"error": "Course not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        course.delete()

        return Response(
            {"message": "Course deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )