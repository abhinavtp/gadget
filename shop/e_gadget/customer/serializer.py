from rest_framework import serializers
from customer.models import Customer
class android(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'