from django.db import models


class Stop(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=25, unique=True, primary_key=True)
    location = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name
    

    
class RouteStop(models.Model):
    route = models.ForeignKey('Route', on_delete=models.CASCADE)
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)
    order = models.PositiveIntegerField
    


class Route(models.Model):
    id = models.CharField(max_length=20, unique=True, primary_key=True)
    name = models.CharField(max_length=150)
    stops = models.ManyToManyField('Stop', through='RouteStop')

    def __str__(self):
        return f"{self.id} ({self.name})"