from django.contrib import admin

# Register your models here.
from .models import Route
from .models import RouteStop, Stop

admin.site.register(Route)
admin.site.register(RouteStop)
admin.site.register(Stop)