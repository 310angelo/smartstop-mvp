from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views
from .views import RouteListView, StopListByRouteView

urlpatterns = [
    path("api/routes/", RouteListView.as_view(), name="route-list"),
    path("api/routes/<int:id>/stops/", StopListByRouteView.as_view(), name="stops-by-route"),
]