from django.shortcuts import render

from django.http import HttpResponse
from rest_framework import generics
from .models import Bus, Route
from backend.serializers import BusSerializer, RouteSerializer, StopSerializer, StopRequestSerializer


def index(request):
    return HttpResponse("Buses index")  # or "Routes index"

class BusListView(generics.ListAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer