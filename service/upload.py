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
    return response.status_code
  
