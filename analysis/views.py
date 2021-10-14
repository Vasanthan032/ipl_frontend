from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.shortcuts import get_object_or_404
from . import models

# Create your views here.
class BatsmanView(LoginRequiredMixin, generic.ListView):
    model = models.Batsman


class BowlerView(LoginRequiredMixin,  generic.ListView):
    model = models.Bowler
