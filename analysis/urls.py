from django.contrib import admin
from django.urls import path
from . import views

app_name = 'analysis'

urlpatterns = [
    #Batsmen
    path('batsmen', views.Batsmen.as_view(), name = 'batsmen'),
    path('batsmen_top10', views.BatsmenTop10.as_view(), name = 'batsmen_top10'),
    path('batsmen_dismissal', views.BatsmenDismissal.as_view(), name = 'batsmen_dismissal'),
    path('batsmen_sixes', views.BatsmenSixes.as_view(), name = 'batsmen_sixes'),
    path('batsmen_fours', views.BatsmenFours.as_view(), name = 'batsmen_fours'),
    path('batsmen_match_wise', views.BatsmenMatchWise.as_view(), name = 'batsmen_match_wise'),

    #Bowler
    path('bowler', views.Bowler.as_view(), name = 'bowler'),
    path('bowler_top10', views.BowlerTop10.as_view(), name = 'bowler_top10'),
    path('bowler_match_wise', views.BowlerMatchWise.as_view(), name = 'bowler_match_wise'),
    # path('bowler_wickets', views.BowlerWickets.as_view(), name = 'bowler_wickets'),
    # path('bowlers_rival', views.BowlerRival.as_view(), name = 'bowlers_rival'),

    #Teams
    path('team', views.Team.as_view(), name = 'team'),
    path('team_stadium_name_with_max_win', views.TeamStadiumNameWithMaxWin.as_view(), name = 'team_stadium_name_with_max_win'),
    path('team_winning_percentage', views.WiningPercentage.as_view(), name = 'team_winning_percentage'),
    path('team_man_of_the_match', views.ManOfTheMatch.as_view(), name = 'team_man_of_the_match'),
]
