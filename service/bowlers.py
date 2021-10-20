import requests
import pandas as pd
from util.graph import Graph

class BowlersService:
  def __init__(self):
    self.BASE_URL = 'http://localhost:8000/api/bowlers'
    self.graph = Graph()
  
  def get_top_10_bowlers(self,year):
    url = f'{self.BASE_URL}/get_top_bowlers'
    params = {'year': year}
    data = requests.get(url, params=params)
    top_10_bowlers = data.json()
    df = pd.DataFrame(top_10_bowlers)
    self.graph.create_barplot(df=df,x_label='Bowler Name', y_label='Wickets Taken',
                          x_col="bowler_name",y_col='total_wickets_taken')
    return top_10_bowlers
