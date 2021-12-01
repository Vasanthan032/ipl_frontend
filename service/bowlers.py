import requests
import pandas as pd
from util.graph import Graph
from django.conf import settings

class BowlersService:
  def __init__(self):
    self.BASE_URL = f'{settings.URL}/api/bowlers'
    self.graph = Graph()
  
  def get_top_10_bowlers(self,request):
    url = f'{self.BASE_URL}/get_top_bowlers'
    data = requests.get(url, data=request)
    top_10_bowlers = data.json()
    df = pd.DataFrame(top_10_bowlers)
    if len(df)>0:
      file_name = self.graph.create_bowler_barplot(df=df,x_label='Bowler Name', y_label='Wickets Taken',
                          x_col="bowler_name",y_col='total_wickets_taken')
      return file_name
    else:
      return None

  def get_bowlers_match_wise(self,request,limit=10,offset=0):
    url = f'{self.BASE_URL}/get_bowlers_match_wise'
    params = {'limit':limit,'offset':offset}
    data = requests.get(url,data=request,params=params)
    try:
      bowlers_match_wise_details = data.json()
      return bowlers_match_wise_details
    except Exception as err:
      return None
