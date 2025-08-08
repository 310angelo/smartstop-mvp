from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views
from .views import StopRequestListView, StopRequestCreateView, StopRequestUpdateView, stop_request_view

urlpatterns = [
    path('', views.index, name='index'),
    path('request/<int:bus_id>/', stop_request_view, name='stop_request'),
    path('api/stoprequests/', StopRequestListView.as_view(), name='stoprequest-list'),
    path('api/stoprequests/new/', StopRequestCreateView.as_view(), name='stoprequest-create'),
    path('api/stoprequests/<int:pk>/', StopRequestUpdateView.as_view(), name='stoprequest-update'),
]