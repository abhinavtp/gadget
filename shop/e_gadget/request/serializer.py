from rest_framework import serializers
from request.models import RequestService
class android(serializers.ModelSerializer):
    class Meta:
        model=RequestService
        fields='__all__'