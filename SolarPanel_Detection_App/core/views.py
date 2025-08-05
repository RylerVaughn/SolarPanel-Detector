from django.shortcuts import render, get_object_or_404  
from .models import Client, Job
from .serializers import ClientSerializer, JobSerializer
from rest_framework import viewsets
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    return render(request, "core/index.html", context={"clients": Client.objects.all()})


class ClientViewSets(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class JobViewSets(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

def client_detail_modal(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    print("\n", client.jobs, "\n")
    return render(request, "core/partials/client_detail_modal.html", {"client": client})

@csrf_exempt
def add_job(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    payment = request.POST.get("payment")
    date = request.POST.get("date")

    Job.objects.create(client=client, payment=payment, date=date)
 
    return JsonResponse({"status": 200})


def add_client(request):
    return render(request, "core/partials/client_request.html")
