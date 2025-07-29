from django.db import models
from buses.models import Bus
from routes.models import Stop, Route, RouteStop

class StopRequest(models.Model):
    id = models.CharField(max_length=20, unique=True, primary_key=True)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return f"Request for {self.stop.name} on bus {self.bus.bus_id} at {self.timestamp}"