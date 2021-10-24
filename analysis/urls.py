from django.contrib import admin
from django.urls import path
from . import views

app_name = 'analysis'

urlpatterns = [
    path('batsmen_top10', views.BatsmenTop10.as_view(), name = 'batsmen_top10'),
    path('batsman_score', views.BatsmanScore.as_view(), name = 'batsman_score'),
    path('batsman_dismissal', views.BatsmanDismissal.as_view(), name = 'batsman_dismissal'),
    path('batsmen_sixes', views.BatsmenSixes.as_view(), name = 'batsmen_sixes'),
    path('batsmen_fours', views.BatsmenFours.as_view(), name = 'batsmen_fours'),
    path('batsman_mom', views.BatsmanMOM.as_view(), name = 'batsman_mom'),
    path('bowler', views.Bowler.as_view(), name = 'bowler'),
    path('bowler_top10', views.BowlerTop10.as_view(), name = 'bowler_top10'),
    path('bowler_match_wise', views.BowlerMatchWise.as_view(), name = 'bowler_match_wise'),
    path('bowler_wickets', views.BowlerWickets.as_view(), name = 'bowler_wickets'),
    path('bowlers_rival', views.BowlerRival.as_view(), name = 'bowlers_rival'),
    path('team', views.Team.as_view(), name = 'team'),
    path('team_stadium_name_with_max_win', views.TeamStadiumNameWithMaxWin.as_view(), name = 'team_stadium_name_with_max_win'),
    path('batsmen', views.Batsmen.as_view(), name = 'batsmen'),
]
