from django.urls import path, include
from . import views
from rest_framework import routers
from .views import ClientViewSets, JobViewSets

client_router = routers.DefaultRouter()
client_router.register(r"clients", ClientViewSets)

job_router = routers.DefaultRouter()
job_router.register(r"jobs", JobViewSets)



urlpatterns = [
    path("", views.index, name="index"),
    path("api/", include(client_router.urls)),
    path("api/", include(job_router.urls)),
    path("clients/<int:client_id>/detail/", views.client_detail_modal, name="client_detail_modal"),
    path("clients/<int:client_id>/addjob/", views.add_job, name="add_job"),
    path("clients/addclient/", views.add_client, name="add_client")
]