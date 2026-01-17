from rest_framework import viewsets, permissions
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()  # You can add custom logic here if needed

    def perform_update(self, serializer):
        serializer.save()  # You can add custom logic here if needed

    def perform_destroy(self, instance):
        instance.delete()  # You can add custom logic here if needed