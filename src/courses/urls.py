from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (
    CoursesAPIView,
    ReviewsAPIView,
    CourseAPIView,
    ReviewAPIView,
    CourseViewSet,
    ReviewViewSet
)

router = SimpleRouter()

router.register('courses', CourseViewSet)
router.register('reviews', ReviewViewSet)

urlpatterns = [
    path('courses/', CoursesAPIView.as_view(), name='courses'),
    path('courses/<int:pk>/', CourseAPIView.as_view(), name='course'),
    path('courses/<int:course_pk>/reviews', ReviewsAPIView.as_view(), name='course_reviews'),
    path('courses/<int:course_pk>/reviews/<int:review_pk>', ReviewAPIView.as_view(), name='course_review'),
    path('reviews/', ReviewsAPIView.as_view(), name='reviews'),
    path('reviews/<int:review_pk>/', ReviewAPIView.as_view(), name='review')
]