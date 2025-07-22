from django.urls import path, include
from . import views
from rest_framework import routers
from .views import ClientViewSets

router = routers.DefaultRouter()
router.register(r"clients", ClientViewSets)

urlpatterns = [
    path("", views.index, name="index"),
    path("api/", include(router.urls))
]