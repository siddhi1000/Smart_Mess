from rest_framework import serializers
from .models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'  # or specify the fields you want to include, e.g., ['id', 'student', 'meal', 'date']