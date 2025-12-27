from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Instructor

# Create your views here.

class InstrList(ListView):
    pass



class InstrDetail(DetailView):

    pass
