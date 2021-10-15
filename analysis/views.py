from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.shortcuts import get_object_or_404
from . import models

# Create your views here.
class BatsmanTop10(LoginRequiredMixin, generic.ListView):
    model = models.Batsman
    template_name = 'analysis/batsman/batsman_top10.html'

class BatsmanMOM(LoginRequiredMixin, generic.ListView):
    model = models.Batsman
    template_name = 'analysis/batsman/batsman_mom.html'

class BatsmanScore(LoginRequiredMixin, generic.ListView):
    model = models.Batsman
    template_name = 'analysis/batsman/batsman_score.html'

class BatsmanDismissal(LoginRequiredMixin, generic.ListView):
    model = models.Batsman
    template_name = 'analysis/batsman/batsman_dismissal.html'

class BatsmanBoundaries(LoginRequiredMixin, generic.ListView):
    model = models.Batsman
    template_name = 'analysis/batsman/batsman_boundaries.html'

class BowlerTop10(LoginRequiredMixin,  generic.ListView):
    model = models.Bowler
    template_name = 'analysis/bowler/bowler_top10.html'

class BowlerWickets(LoginRequiredMixin,  generic.ListView):
    model = models.Bowler
    template_name = 'analysis/bowler/bowler_wickets.html'

class BowlerRival(LoginRequiredMixin,  generic.ListView):
    model = models.Bowler
    template_name = 'analysis/bowler/bowler_rival.html'
