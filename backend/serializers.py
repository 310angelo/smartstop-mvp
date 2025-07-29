# serializers.py

from rest_framework import serializers
from buses.models import Bus
from routes.models import Route, Stop
from stoprequests.models import StopRequest

class StopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stop
        fields = ['id', 'name', 'location']

class RouteSerializer(serializers.ModelSerializer):
    stops = StopSerializer(many=True, read_only=True)
    class Meta:
        model = Route
        fields = ['id', 'name', 'stops']

class BusSerializer(serializers.ModelSerializer):
    route = RouteSerializer(read_only=True)

    class Meta:
        model = Bus
        fields = ['id', 'route']

class StopRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = StopRequest
        fields = ['id', 'bus', 'stop', 'timestamp']
        read_only_fields = ['timestamp']