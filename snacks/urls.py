from django.contrib import admin
from django.urls import path

from .views import SnackListView

urlpatterns = [
    path('',SnackListView.as_view(),name='snacks')
]