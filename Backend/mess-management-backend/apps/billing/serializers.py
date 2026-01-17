from rest_framework import serializers
from ..models import Billing

class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billing
        fields = '__all__'  # Include all fields from the Billing model

class BillingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billing
        fields = ['id', 'student', 'amount', 'date', 'status']  # Specify fields for detailed view