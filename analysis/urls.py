from django.contrib import admin
from django.urls import path
from . import views

app_name = 'analysis'

urlpatterns = [
    path('batsman_top10', views.BatsmanTop10.as_view(), name = 'batsman_top10'),
    path('batsman_score', views.BatsmanScore.as_view(), name = 'batsman_score'),
    path('batsman_dismissal', views.BatsmanDismissal.as_view(), name = 'batsman_dismissal'),
    path('batsman_boundaries', views.BatsmanBoundaries.as_view(), name = 'batsman_boundaries'),
    path('batsman_mom', views.BatsmanMOM.as_view(), name = 'batsman_mom'),
    path('bowler', views.Bowler.as_view(), name = 'bowler'),
    path('bowler_top10', views.BowlerTop10.as_view(), name = 'bowler_top10'),
    path('bowler_wickets', views.BowlerWickets.as_view(), name = 'bowler_wickets'),
    path('bowlers_rival', views.BowlerRival.as_view(), name = 'bowlers_rival'),
]
