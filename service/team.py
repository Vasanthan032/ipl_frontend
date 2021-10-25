import requests
import pandas as pd
from util.graph import Graph

class TeamService:
  def __init__(self):
    self.BASE_URL = 'http://localhost:8000/api/match_details'
    self.graph = Graph()

  def get_stadium_name_with_max_win(self,year):
    url = f'{self.BASE_URL}/team_stadium_name_with_max_win'
    params = {'year': year}
    data = requests.get(url, params=params)
    result = data.json()
    return result

  def get_team_home_ground(self):
    url = 'http://localhost:8000/api/team/get_team_home_ground'
    data = requests.get(url)
    result = data.json()
    return result

  def get_winning_percentage(self,year):
    url = f'{self.BASE_URL}/winning_percentage'
    data = requests.get(url)
    winning_percentage = data.json()
    df = pd.DataFrame(winning_percentage)
    file_name = self.graph.create_pi_chart(df=df,title='Winning Percentage of a Team, if they won the toss', year=year)
    return file_name
