from django.contrib import admin
from django.urls import path

from .views import SnackListView,DetailView

urlpatterns = [
    path('',SnackListView.as_view(),name='snacks'),
    path('detail/<pk>',DetailView.as_view(),name='detail')
]