from django.shortcuts import render

from django.http import HttpResponse
from rest_framework import generics
from .models import Route, Stop
from backend.serializers import BusSerializer, RouteSerializer, StopSerializer, StopRequestSerializer

class RouteListView(generics.ListAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class StopListByRouteView(generics.ListAPIView):
    serializer_class = StopSerializer

    def get_queryset(self):
        route_id = self.kwargs['route_id']
        return Stop.objects.filter(routestop__route__id=route_id).order_by('routestop__order')