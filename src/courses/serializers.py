from rest_framework import serializers

from .models import Course, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Review
        fields = (
            'id',
            'course',
            'name',
            'comment',
            'rating',
            'created_at',
            'updated_at',
            'active'
        )

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'url',
            'created_at',
            'updated_at',
            'active'
        )