from django.db.models import query
from rest_framework import generics, viewsets, mixins
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Course, Review
from .serializers import CourseSerializer, ReviewSerializer

"""
API Version 1
"""

class CoursesAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class ReviewsAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        if self.kwargs.get('course_pk'):
            return self.queryset.filter(course_id=self.kwargs.get('course_pk'))
        return self.queryset.all()

class ReviewAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_object(self):
        if self.kwargs.get('course_pk'):
            return get_object_or_404(self.get_queryset(),
                course_id=self.kwargs.get('course_pk'),
                pk=self.kwargs.get('review_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('review_pk'))

"""
API Version 2
"""

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=['get'])
    def reviews(self, request, pk=None):
        course = self.get_object()
        serializer = ReviewSerializer(course.reviews.all(), many=True)
        return Response(serializer.data)

# class ReviewViewSet(viewsets.ModelViewSet):
class ReviewViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# Version 1

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# from .models import Course, Review
# from .serializers import CourseSerializer, ReviewSerializer

# class CourseAPIView(APIView):
#     """
#     Courses API
#     """
#     def get(self, request):
#         courses = Course.objects.all()
#         serializer = CourseSerializer(courses, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = CourseSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# class ReviewAPIView(APIView):
#     """
#     Reviews API
#     """
#     def get(self, request):
#         reviews = Review.objects.all()
#         serializer = ReviewSerializer(reviews, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = ReviewAPIView(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)