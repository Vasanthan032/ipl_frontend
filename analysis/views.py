from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.shortcuts import get_object_or_404
from . import models,forms
from pathlib import Path
from service.bowlers import BowlersService
from service.batsmen import BatsmenService
from service.team import TeamService

# Create your views here.
#Batsmen's View classes
class Batsmen(LoginRequiredMixin,  generic.ListView):
    def get(self,request):
        return render(request,'analysis/batsmen/home.html')

class BatsmenTop10(LoginRequiredMixin,  generic.ListView):
    def get(self,request):
        form_class = forms.FilterForm
        return render(request,'analysis/batsmen/batsmen_top10.html',{'form':form_class})
    def post(self,request):
        data = request.POST
        batsmen_service = BatsmenService()
        file_path = batsmen_service.get_top_10_batsmen(data['year'])
        form_class = forms.FilterForm
        return render(request,'analysis/batsmen/batsmen_top10.html',{'form':form_class,
                      'file_path':file_path})

class BatsmenDismissal(LoginRequiredMixin, generic.ListView):
    def get(self,request):
        data = request.POST
        batsmen_service = BatsmenService()
        data = batsmen_service.get_top_batsman_dismissal()
        form_class = forms.FilterForm
        return render(request,'analysis/batsmen/batsmen_dismissal.html',{'form':form_class,
                      'data':data})
    def post(self,request):
        data = request.POST
        batsmen_service = BatsmenService()
        data = batsmen_service.get_top_batsman_dismissal()
        form_class = forms.FilterForm
        return render(request,'analysis/batsmen/batsmen_dismissal.html',{'form':form_class,
                      'data':data})


class BatsmenSixes(LoginRequiredMixin, generic.ListView):
    def get(self,request):
        form_class = forms.FilterForm
        return render(request,'analysis/batsmen/batsmen_sixes.html',{'form':form_class})
    def post(self,request):
        data = request.POST
        batsmen_service = BatsmenService()
        file_path = batsmen_service.get_top_six_hitters(data['year'])
        form_class = forms.FilterForm
        return render(request,'analysis/batsmen/batsmen_sixes.html',{'form':form_class,
                      'file_path':file_path})

class BatsmenFours(LoginRequiredMixin, generic.ListView):
    def get(self,request):
        form_class = forms.FilterForm
        return render(request,'analysis/batsmen/batsmen_fours.html',{'form':form_class})
    def post(self,request):
        data = request.POST
        batsmen_service = BatsmenService()
        file_path = batsmen_service.get_top_four_hitters(data['year'])
        form_class = forms.FilterForm
        return render(request,'analysis/batsmen/batsmen_fours.html',{'form':form_class,
                      'file_path':file_path})

class BatsmenMatchWise(LoginRequiredMixin,  generic.ListView):
    def get(self,request):
        form_class = forms.FilterForm
        return render(request,'analysis/batsmen/batsmen_match_wise.html',{'form':form_class})
    def post(self,request):
        data = request.POST
        batsmen_service = BatsmenService()
        match_wise_details = batsmen_service.get_batsmen_match_wise(data['year'])
        form_class = forms.FilterForm
        return render(request,'analysis/batsmen/batsmen_match_wise.html',{'form':form_class,
                      'match_wise_details':match_wise_details})

#Bowler's View classes
class Bowler(LoginRequiredMixin,  generic.ListView):
    def get(self,request):
        return render(request,'analysis/bowler/home.html')

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
        bowler_service = BowlersService()
        match_wise_details = bowler_service.get_bowlers_match_wise(data['year'])
        form_class = forms.FilterForm
        return render(request,'analysis/bowler/bowler_match_wise.html',{'form':form_class,
                      'match_wise_details':match_wise_details})

#Teams's View classes
class Team(LoginRequiredMixin,  generic.ListView):
    def get(self,request):
        return render(request,'analysis/team/home.html')

class TeamStadiumNameWithMaxWin(LoginRequiredMixin,  generic.ListView):
    def get(self,request):
        form_class = forms.FilterForm
        return render(request,'analysis/team/team_stadium_name_max_win.html',{'form':form_class})
    def post(self,request):
        data = request.POST
        team_service = TeamService()
        data = team_service.get_stadium_name_with_max_win(data['year'])
        form_class = forms.FilterForm
        return render(request,'analysis/team/team_stadium_name_max_win.html',{'form':form_class,
                      'data':data})

class WiningPercentage(LoginRequiredMixin,  generic.ListView):
    def get(self,request):
        form_class = forms.FilterForm
        return render(request,'analysis/team/team_winning_percentage.html',{'form':form_class})
    def post(self,request):
        data = request.POST
        team_Service = TeamService()
        file_path = team_Service.get_winning_percentage(data['year'])
        form_class = forms.FilterForm
        return render(request,'analysis/team/team_winning_percentage.html',{'form':form_class,
                      'file_path':file_path})

class ManOfTheMatch(LoginRequiredMixin,  generic.ListView):
    def get(self,request):
        form_class = forms.FilterForm
        return render(request,'analysis/team/team_man_of_the_match.html',{'form':form_class})
    def post(self,request):
        data = request.POST
        team_Service = TeamService()
        file_path = team_Service.get_man_of_the_match(data['year'])
        form_class = forms.FilterForm
        return render(request,'analysis/team/team_man_of_the_match.html',{'form':form_class,
                      'file_path':file_path})
