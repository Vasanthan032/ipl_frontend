import requests
import pandas as pd
from django.http import QueryDict
class UploadService:
  def __init__(self):
    self.BASE_URL = 'http://localhost:8000/api'
  
  def match_details(self,request):
    url = f'{self.BASE_URL}/match_details/upload'
    response = requests.post(url, files=request.FILES)
    return response.status_code

  def ball_details(self,request):
    url = f'{self.BASE_URL}/ball_details/upload'
    response = requests.post(url, files=request.FILES)
    if response.status_code == 201:
      team_url = f'{self.BASE_URL}/team/insert'
      bowlers_url = f'{self.BASE_URL}/bowlers/insert'
      batsmen_url = f'{self.BASE_URL}/batsmen/insert'
      team_response = requests.post(team_url)
      if team_response.status_code == 201:
        bowlers_response = requests.post(bowlers_url)
        if bowlers_response.status_code == 201:
          batsmen_response = requests.post(batsmen_url)
          return batsmen_response.status_code

  
