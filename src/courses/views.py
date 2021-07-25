from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Course, Review
from .serializers import CourseSerializer, ReviewSerializer

class CourseAPIView(APIView):
    """
    Courses API
    """
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

class ReviewAPIView(APIView):
    """
    Reviews API
    """
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)