from rest_framework import serializers
from .models import Client, Job

class ClientSerializer(serializers.ModelSerializer):
    notes = serializers.CharField(allow_blank=True)


    class Meta:
        model = Client
        fields = "__all__"


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"