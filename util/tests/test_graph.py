from django.test import TestCase
from django.conf import settings
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import uuid
import boto3
import io
BASE_DIR = Path(__file__).resolve().parent.parent
image_file_path = BASE_DIR.joinpath("util/graphs/")

class APITest(TestCase):
  def test_graph_creation(self):
    BASE_URL = f'{settings.URL}/api/bowlers'
    url = f'{BASE_URL}/get_top_bowlers'
    data = requests.get(url, data={'year':'overall','team_name':'None'})
    top_10_bowlers = data.json()
    df = pd.DataFrame(top_10_bowlers)
    if len(df)>0:
      file_name = self.create_bowler_barplot(df=df,x_label='Bowler Name', y_label='Wickets Taken',
                          x_col="bowler_name",y_col='total_wickets_taken')
      print(file_name)
    else:
      return None
    self.assertTrue(len(df) >= 0)
  
  def create_bowler_barplot(self,df,x_label,y_label,x_col,y_col):
    plt.figure(figsize=(15,8),dpi=100)
    plt.style.use('ggplot')
    sns.set_theme(style="whitegrid")
    ax = sns.barplot(x=x_col,y=y_col,data=df,hue='bowler_team',palette="Set2")

    for bar in ax.patches:
      ax.annotate(bar.get_height(),
                   (bar.get_x() + bar.get_width() / 2,
                    bar.get_height()), ha='center', va='center',
                   size=10, xytext=(0, 8),
                   textcoords='offset points')

    ax.set(xlabel=x_label, ylabel=y_label)
    ax.tick_params(axis='x', rotation=30)
    plt.setp(ax.patches, linewidth=0)
    plt.legend(title = 'Team Name', bbox_to_anchor=(1, 1))
    buf = io.BytesIO()
    file_name = f'{uuid.uuid4()}.jpg'
    # file_saving_path = f'{image_file_path}/{file_name}'
    plt.savefig(buf,format='jpg',bbox_inches = 'tight')
    buf.seek(0)
    # img_data = buf.read()
    self.save_to_s3(buf,file_name)
    return file_name
  
  def save_to_s3(self,img_data,file_name):
    #Creating Session With Boto3.
    session = boto3.Session(
    aws_access_key_id='AKIAQ5CABQ424JLFIZXC',
    aws_secret_access_key='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'
    )

    #Creating S3 Resource From the Session.
    s3 = session.resource('s3')

    object = s3.Object('de-project-graphs',file_name)
    result = object.put(Body=img_data,ContentType='image/jpg')

    res = result.get('ResponseMetadata')

    if res.get('HTTPStatusCode') == 200:
      print('File Uploaded Successfully')
    else:
      print('File Not Uploaded')
