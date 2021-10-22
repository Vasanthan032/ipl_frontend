import requests

class TeamService:
  def __init__(self):
    self.BASE_URL = 'http://localhost:8000/api/match_details'
  
  def get_stadium_name_with_max_win(self,year):
    url = f'{self.BASE_URL}/team_stadium_name_with_max_win'
    params = {'year': year}
    data = requests.get(url, params=params)
    result = data.json()
    return result
  
  def get_team_home_ground(self):
    url = f'{self.BASE_URL}/get_team_home_ground'
    data = requests.get(url)
    result = data.json()
    return result
