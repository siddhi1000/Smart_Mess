from rest_framework import serializers
from ..models import Feedback

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'student', 'meal', 'rating', 'comments', 'created_at']
        read_only_fields = ['id', 'created_at']