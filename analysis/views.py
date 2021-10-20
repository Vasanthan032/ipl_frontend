from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.shortcuts import get_object_or_404
from . import models,forms
from pathlib import Path

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
    def get(self,request):
        form_class = forms.FilterForm
        return render(request,'analysis/bowler/bowler_top10.html',{'form':form_class})
    def post(self,request):
        data = request.POST
        graph_file_path = Path('static/graph/bowlers/top_10_bowler.jpg')
        form_class = forms.FilterForm
        return render(request,'analysis/bowler/bowler_top10.html',{'form':form_class,
                      'graph_file_path':graph_file_path})

class Bowler(LoginRequiredMixin,  generic.ListView):
    def get(self,request):
        return render(request,'analysis/bowler/home.html')
    def post(self,request):
        pass

class BowlerWickets(LoginRequiredMixin,  generic.ListView):
    model = models.Bowler
    template_name = 'analysis/bowler/bowler_wickets.html'

class BowlerRival(LoginRequiredMixin,  generic.ListView):
    model = models.Bowler
    template_name = 'analysis/bowler/bowler_rival.html'
