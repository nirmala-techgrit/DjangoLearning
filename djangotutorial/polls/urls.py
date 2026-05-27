from django.urls import path, include

from rest_framework.routers import DefaultRouter
from polls.views.student import StudentListCreateAPIView, StudentDetailAPIView, StudentAPIUsingGenericAPIView
from polls.views.course import course_details
from polls.views.instructor import InstructorViewSet

# Router for ModelViewSet
router = DefaultRouter()

router.register(
    'instructors-viewset',
    InstructorViewSet,
    basename='instructors-viewset'
)


urlpatterns = [

    path(
        'students/',
        StudentListCreateAPIView.as_view(),
        name='student-list-create'
    ),

    path(
        'students/<uuid:pk>/',
        StudentDetailAPIView.as_view(),
        name='student-detail-using-generic-apiview'
    ),
     path(
        "students-generic-apiview/",
        StudentAPIUsingGenericAPIView.as_view(),
        name="student-list-create-detail-using-generic-apiview"
    ),

    path(
        "students-generic-apiview/<int:pk>/",
        StudentAPIUsingGenericAPIView.as_view(),
        name="student-detail"
    ),
     path(
        'course-details/',
        course_details,
        name='course-details'
    ),
    path(
        '',
        include(router.urls)
    ),
]