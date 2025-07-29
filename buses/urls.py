from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views
from .views import BusListView

urlpatterns = [
    path('', views.index, name='index'),
    path('api/buses/', BusListView.as_view(), name='buslist-view'),
]