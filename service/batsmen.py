import requests
import pandas as pd
from util.graph import Graph

class BatsmenService:
  def __init__(self):
    self.BASE_URL = 'http://localhost:8000/api/batsmen'
    self.graph = Graph()   
  def get_top_10_batsmen(self,year):
      url = f'{self.BASE_URL}/get_top_batsmen'
      params = {'year': year}
      data = requests.get(url, params=params)
      top_10_batsmen = data.json()
      df = pd.DataFrame(top_10_batsmen)
      file_name = self.graph.create_batsmen_barplot(df=df,x_label='Batsman Name', y_label='Runs Scored',
                          x_col="batsman_name",y_col='runs_scored')
      return file_name 

  def get_top_six_hitters(self,year):
      url = f'{self.BASE_URL}/get_six_hitters'
      params = {'year': year}
      data = requests.get(url, params=params)
      top_six_hitters = data.json()
      df = pd.DataFrame(top_six_hitters)
      file_name = self.graph.create_batsmen_barplot(df=df,x_label='Batsman Name', y_label='Sixes',
                          x_col="batsman_name",y_col='sixes')
      return file_name 

  def get_top_four_hitters(self,year):
      url = f'{self.BASE_URL}/get_four_hitters'
      params = {'year': year}
      data = requests.get(url, params=params)
      top_four_hitters = data.json()
      df = pd.DataFrame(top_four_hitters)
      file_name = self.graph.create_batsmen_barplot(df=df,x_label='Batsman Name', y_label='Fours',
                          x_col="batsman_name",y_col='fours')
      return file_name

  def get_top_batsman_dismissal(self,year):
      url = f'{self.BASE_URL}/get_batsmen_vs_bowler'
      data = requests.get(url)
      batsman_bowler_dismissal = data.json()
      return batsman_bowler_dismissal
