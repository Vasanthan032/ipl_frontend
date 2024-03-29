import requests
import pandas as pd
from util.graph import Graph
from django.conf import settings

class TeamService:
  def __init__(self):
    self.BASE_URL = f'{settings.URL}/api/match_details'
    self.graph = Graph()

  def get_stadium_name_with_max_win(self,year,team_name):
    url = f'{self.BASE_URL}/team_stadium_name_with_max_win'
    params = {'year': year, 'team_name': team_name}
    data = requests.get(url, params=params)
    result = data.json()
    return result

  def get_team_home_ground(self):
    url = 'http://localhost:8000/api/team/get_team_home_ground'
    data = requests.get(url)
    result = data.json()
    return result

  def get_winning_percentage(self,year,team_name):
    url = f'{self.BASE_URL}/winning_percentage'
    params = {'year': year, 'team_name':team_name}
    data = requests.get(url, params)
    winning_percentage = data.json()

    df = pd.DataFrame(winning_percentage)
    file_name = self.graph.create_pi_chart(df=df,title='Winning Percentage of a Team, if they won the toss', year=year, team_name=team_name)
    return file_name

  def get_man_of_the_match(self,year, limit=10):
    url = f'{self.BASE_URL}/man_of_the_match'
    params = {'year': year}
    data = requests.get(url, params=params)
    man_of_the_match = data.json()
    df = pd.DataFrame(man_of_the_match)
    file_name = self.graph.create_mom_barplot(df=df,x_label='Player Name', y_label='Number of Man of the Match tittle',
                          x_col="name",y_col='count')
    return file_name
