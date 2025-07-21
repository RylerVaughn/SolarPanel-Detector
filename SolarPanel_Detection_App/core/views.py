from django.shortcuts import render
from .models import Marker
from .serializers import MarkerSerializer
from rest_framework import viewsets

# Create your views here.
def index(request):
    return render(request, "core/index.html")


class MarkerViewSets(viewsets.ModelViewSet):
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer