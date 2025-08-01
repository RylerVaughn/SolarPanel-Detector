from django.urls import path, include
from . import views
from rest_framework import routers
from .views import ClientViewSets

router = routers.DefaultRouter()
router.register(r"clients", ClientViewSets)

urlpatterns = [
    path("", views.index, name="index"),
    path("api/", include(router.urls)),
    path("clients/<int:client_id>/detail/", views.client_detail_modal, name="client_detail_modal"),
    path("clients/<int:client_id>/addjob/", views.add_job, name="add_job"),
    path("clients/addclient/", views.add_client, name="add_client")
]