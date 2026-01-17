from rest_framework import serializers
from .models import Meal

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'  # or specify the fields you want to include, e.g., ['id', 'name', 'description', 'price']