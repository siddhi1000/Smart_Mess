from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Meal
from .serializers import MealSerializer

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Optionally filter meals based on user role or other criteria
        return super().get_queryset()