from rest_framework import viewsets
from rest_framework.response import Response
from .models import Billing
from .serializers import BillingSerializer

class BillingViewSet(viewsets.ModelViewSet):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        billing = self.get_object()
        serializer = self.get_serializer(billing)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        billing = serializer.save()
        return Response(self.get_serializer(billing).data, status=201)

    def update(self, request, pk=None):
        billing = self.get_object()
        serializer = self.get_serializer(billing, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        billing = serializer.save()
        return Response(self.get_serializer(billing).data)

    def destroy(self, request, pk=None):
        billing = self.get_object()
        billing.delete()
        return Response(status=204)