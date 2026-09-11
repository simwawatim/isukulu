from core.Views.Dashboard import Dashboard
from django.urls import path

urlpatterns = [
    path("dashboard/", Dashboard, name="dashboard"),
]