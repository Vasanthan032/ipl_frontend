import requests
import pandas as pd
from util.graph import Graph

class BatsmenService:
  def __init__(self):
    self.BASE_URL = 'http://localhost:8000/api/batsmen'
    self.graph = Graph()
  def get_top_10_batsmen(self,request):
      url = f'{self.BASE_URL}/get_top_batsmen'
      data = requests.get(url, data=request)
      top_10_batsmen = data.json()
      df = pd.DataFrame(top_10_batsmen)
      if len(df)>0:
          file_name = self.graph.create_batsmen_barplot(df=df, year = request['year'],
                          team_name = request['team_name'],category='batsmen', 
                          color='c', x_label='Batsman Name', y_label='Runs Scored',
                          x_col="batsman_name",y_col='runs_scored')
          return file_name
      else:
          return None

  def get_top_six_hitters(self,request):
      url = f'{self.BASE_URL}/get_six_hitters'
      data = requests.get(url, data=request)
      top_six_hitters = data.json()
      df = pd.DataFrame(top_six_hitters)
      
      if len(df)>0:
          file_name = self.graph.create_batsmen_barplot(df=df, year = request['year'],
                          team_name = request['team_name'],category='six hitters',
                          color='limegreen',x_label='Batsman Name', y_label='Sixes',
                          x_col="batsman_name",y_col='sixes')
          return file_name
      else:
          return None

  def get_top_four_hitters(self,request):
      url = f'{self.BASE_URL}/get_four_hitters'
      data = requests.get(url, data=request)
      top_four_hitters = data.json()
      df = pd.DataFrame(top_four_hitters)
      
      if len(df)>0:
          file_name = self.graph.create_batsmen_barplot(df=df,year = request['year'],
                          team_name = request['team_name'],category='four hitters',
                          color='orangered', x_label='Batsman Name', y_label='Fours',
                          x_col="batsman_name",y_col='fours')
          return file_name
      else:
          return None

  def get_top_batsman_dismissal(self):
      url = f'{self.BASE_URL}/get_batsmen_vs_bowler'
      data = requests.get(url)
      batsman_bowler_dismissal = data.json()
      return batsman_bowler_dismissal

  def get_batsmen_match_wise(self,year,limit=10,offset=0):
      url = f'{self.BASE_URL}/get_batsmen_details_match_wise'
      params = {'year': year,'limit':limit,'offset':offset}
      data = requests.get(url, params=params)
      batsmen_match_wise_details = data.json()
      return batsmen_match_wise_details
