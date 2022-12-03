from django.shortcuts import render
from .models import Snack
from django.views.generic import ListView,DetailView

class SnackListView(ListView):
    template_name='snack_list.html'
    model=Snack
class DetailView(DetailView):
    template_name='snack_detail.html'
    model=Snack
    

# Create your views here.
