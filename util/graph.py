import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import uuid
import io
import boto3
BASE_DIR = Path(__file__).resolve().parent.parent

class Graph:
  def __init__(self):
    self.base_file_path = BASE_DIR.joinpath("users/static/")
    self.S3_GRAPH_FILE_PATH = 'https://de-project-graphs.s3.us-east-2.amazonaws.com'
    #Creating Session With Boto3.
    self.session = boto3.Session(
    aws_access_key_id='AKIAQ5CABQ424JLFIZXC',
    aws_secret_access_key='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'
    )

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
    plt.savefig(buf,format='jpg',bbox_inches = 'tight')
    buf.seek(0)
    file_name = f'{uuid.uuid4()}.jpg'
    s3_result = self.save_to_s3(buf,file_name)
    if s3_result:
      file_path = f'{self.S3_GRAPH_FILE_PATH}/{file_name}'
      return file_path
    return None

  def create_batsmen_barplot(self,df,year,team_name,category,color, x_label,y_label,x_col,y_col):
    plt.figure(figsize=(15,8),dpi=100)
    plt.style.use('ggplot')
    sns.set_theme(style="darkgrid")
    ax = sns.barplot(y=x_col,x=y_col,data=df, hue='team',palette="tab10")
    ax.set(xlabel=y_label, ylabel='')

    if team_name == 'None':
      ax.set_title(f'{year.upper()} TOP10 {category.upper()}', size=15)
      plt.legend(title = 'Team Name')
    else:
      ax.set_title(f'{str(team_name).upper()} {year.upper()} TOP10 {category.upper()}', size=15)

    for bar in ax.patches:
      ax.annotate('{:,.0f}'.format(bar.get_width()),
                   (bar.get_width(), bar.get_y() + bar.get_height() / 2),
                   size=12, xytext=(5, 0),
                   textcoords='offset points')
    
    buf = io.BytesIO()
    plt.savefig(buf,format='jpg',bbox_inches = 'tight')
    buf.seek(0)
    file_name = f'{uuid.uuid4()}.jpg'
    s3_result = self.save_to_s3(buf,file_name)
    if s3_result:
      file_path = f'{self.S3_GRAPH_FILE_PATH}/{file_name}'
      return file_path
    return None
    

  def create_pi_chart(self,df,title,year,team_name):
    plt.figure(figsize=(12,6),dpi=100)
    x = df[year]['percentage']
    y = 100 - x
    ax = plt.pie([x,y], explode=[0.06,0], labels=['Toss won', 'Toss lost'], autopct='%1.1f%%',shadow=True, startangle=50)
    plt.title(f'Winning Percentage if won the toss by team: {team_name} in year: {year}')
    buf = io.BytesIO()
    plt.savefig(buf,format='jpg',bbox_inches = 'tight')
    buf.seek(0)
    file_name = f'{uuid.uuid4()}.jpg'
    s3_result = self.save_to_s3(buf,file_name)
    if s3_result:
      file_path = f'{self.S3_GRAPH_FILE_PATH}/{file_name}'
      return file_path
    return None

  def create_mom_barplot(self,df,x_label,y_label,x_col,y_col):
    plt.figure(figsize=(12,6),dpi=100)
    sns.set_theme(style="whitegrid")
    ax = sns.barplot(x=df.loc[x_col],y=df.loc[y_col],palette="rocket")
    ax.set(xlabel=x_label, ylabel=y_label)
    ax.tick_params(axis='x', rotation=30)
    buf = io.BytesIO()
    plt.savefig(buf,format='jpg',bbox_inches = 'tight')
    buf.seek(0)
    file_name = f'{uuid.uuid4()}.jpg'
    s3_result = self.save_to_s3(buf,file_name)
    if s3_result:
      file_path = f'{self.S3_GRAPH_FILE_PATH}/{file_name}'
      return file_path
    return None

  def save_to_s3(self,img_data,file_name):
    #Creating S3 Resource From the Session.
    s3 = self.session.resource('s3')
    res = False
    try:
      object = s3.Object('de-project-graphs',file_name)
      result = object.put(Body=img_data,ContentType='image/jpg')
      res = result.get('ResponseMetadata')
      return res.get('HTTPStatusCode') == 200
    except Exception as err:
      print(f'Error while uploading {err}')
    
    return res