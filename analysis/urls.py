from django.contrib import admin
from django.urls import path
from . import views

app_name = 'analysis'

urlpatterns = [
    path('batsman', views.BatsmanView.as_view(template_name = 'analysis/batsman.html'), name = 'batsman'),
    path('bowler', views.BowlerView.as_view(template_name = 'analysis/bowler.html'), name = 'bowler'),
]
