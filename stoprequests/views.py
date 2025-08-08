from django.shortcuts import render, get_object_or_404

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


def stop_request_view(request, bus_id):
    bus = get_object_or_404(Bus, id=bus_id)
    route = bus.route  # Assuming Bus has a ForeignKey to Route
    stops = Stop.objects.filter(route=route)
    if request.method == "POST":
        stop_id = request.POST.get("stop")
        # Handle the stop request logic here
        # ...
    return render(request, "stop_request.html", {"bus": bus, "route": route, "stops": stops})