from django.shortcuts import render
from .models import Snack
from django.views.generic import ListView

class SnackListView(ListView):
    template_name='snack_list.html'
    model=Snack

# Create your views here.
