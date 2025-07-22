from rest_framework import serializers
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    notes = serializers.CharField(allow_blank=True)


    class Meta:
        model = Client
        fields = "__all__"