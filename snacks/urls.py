from django.contrib import admin
from django.urls import path

from .views import SnackListView,detail_view

urlpatterns = [
    path('',SnackListView.as_view(),name='snacks'),
]