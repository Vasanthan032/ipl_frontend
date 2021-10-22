from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.shortcuts import get_object_or_404
from . import models,forms
from pathlib import Path
from service.bowlers import BowlersService

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
        bowler_Service = BowlersService()
        file_path = bowler_Service.get_top_10_bowlers(data['year'])
        form_class = forms.FilterForm
        return render(request,'analysis/bowler/bowler_top10.html',{'form':form_class,
                      'file_path':file_path})

class BowlerMatchWise(LoginRequiredMixin,  generic.ListView):
    def get(self,request):
        form_class = forms.FilterForm
        return render(request,'analysis/bowler/bowler_match_wise.html',{'form':form_class})
    def post(self,request):
        data = request.POST
        bowler_Service = BowlersService()
        match_wise_details = bowler_Service.get_bowlers_match_wise(data['year'])
        form_class = forms.FilterForm
        return render(request,'analysis/bowler/bowler_match_wise.html',{'form':form_class,
                      'match_wise_details':match_wise_details})

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
