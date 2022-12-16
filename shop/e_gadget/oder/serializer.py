from rest_framework import serializers
from oder.models import Order
class android(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'