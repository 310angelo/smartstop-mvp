from django.db import models
from routes.models import Route

class Bus(models.Model):
    id = models.CharField(max_length=20, primary_key=True, unique=True)
    route = models.ForeignKey(Route, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return f"{self.bus_id} ({self.route})"
    