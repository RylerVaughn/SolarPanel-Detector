from rest_framework import serializers
from .models import Marker

class MarkerSerializer(serializers.ModelSerializer):
    notes = serializers.CharField(allow_blank=True)


    class Meta:
        model = Marker
        fields = "__all__"