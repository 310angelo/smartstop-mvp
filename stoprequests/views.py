from django.shortcuts import render

from django.http import HttpResponse

from django.shortcuts import render

from django.http import HttpResponse
from rest_framework import generics
from .models import Bus, Route, Stop, StopRequest
from backend.serializers import BusSerializer, RouteSerializer, StopSerializer, StopRequestSerializer

def index(request):
    return HttpResponse("StopRequests index")


class StopRequestCreateView(generics.CreateAPIView):
    serializer_class = StopRequestSerializer
    queryset = StopRequest.objects.all()

class StopRequestListView(generics.ListAPIView):
    queryset = StopRequest.objects.all()
    serializer_class = StopRequestSerializer

class StopRequestUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StopRequest.objects.all()
    serializer_class = StopRequestSerializer