from django.shortcuts import render, get_object_or_404, redirect   
from .models import Client, Job
from .serializers import ClientSerializer
from rest_framework import viewsets


# Create your views here.
def index(request):
    return render(request, "core/index.html", context={"clients": Client.objects.all()})


class ClientViewSets(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

def client_detail_modal(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    return render(request, "core/partials/client_detail_modal.html", {"client": client})


def add_job(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    payment = request.POST.get("payment")
    date = request.POST.get("date")

    Job.objects.create(client=client, payment=payment, date=date)

    return redirect("client_detail_modal", client_id=client.id)