from rest_framework import serializers
from rating.models import Rating
class android(serializers.ModelSerializer):
    class Meta:
        model=Rating
        fields='__all__'