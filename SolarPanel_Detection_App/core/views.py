from django.shortcuts import render
from .models import Client
from .serializers import ClientSerializer
from rest_framework import viewsets

# Create your views here.
def index(request):
    return render(request, "core/index.html")


class ClientViewSets(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer