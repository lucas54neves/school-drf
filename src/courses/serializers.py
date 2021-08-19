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
    # Nested Relationship -> One-to-one
    # reviews = ReviewSerializer(many=True, read_only=True)

    # Hyperlinked Related Field -> Restful
    # reviews = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='review-detail'
    # )

    # Primary Key Related Field -> Performance
    reviews = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'url',
            'created_at',
            'updated_at',
            'active',
            'reviews'
        )