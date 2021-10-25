import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import uuid
BASE_DIR = Path(__file__).resolve().parent.parent

class Graph:
  def __init__(self):
    self.base_file_path = BASE_DIR.joinpath("users/static/")

  def create_barplot(self,df,x_label,y_label,x_col,y_col):
    plt.figure(figsize=(12,6),dpi=100)
    sns.set_theme(style="whitegrid")
    ax = sns.barplot(x=x_col,y=y_col,data=df,palette="rocket")
    ax.set(xlabel=x_label, ylabel=y_label)
    ax.tick_params(axis='x', rotation=30)
    file_path = f'graph/bowlers/{uuid.uuid4()}.jpg'
    file_saving_path = f'{self.base_file_path}/{file_path}'
    plt.savefig(file_saving_path,bbox_inches = 'tight')
    return file_path


  def create_batsmen_barplot(self,df,x_label,y_label,x_col,y_col):
    plt.figure(figsize=(12,6),dpi=100)
    sns.set_theme(style="whitegrid")
    ax = sns.barplot(x=x_col,y=y_col,data=df,palette="rocket")
    ax.set(xlabel='', ylabel='')
    ax.tick_params(axis='x', rotation=30)
    file_path = f'graph/batsmen/{uuid.uuid4()}.jpg'
    file_saving_path = f'{self.base_file_path}/{file_path}'
    plt.savefig(file_saving_path,bbox_inches = 'tight')
    return file_path

  def create_pi_chart(self,df,title,year):
    plt.figure(figsize=(12,6),dpi=100)
    x = df[year]['percentage']
    y = 100 - x
    ax = plt.pie([x,y], explode=[0.06,0], labels=['Toss won', 'Toss lost'], autopct='%1.1f%%',shadow=True, startangle=50)
    file_path = f'graph/team/{uuid.uuid4()}.jpg'
    file_saving_path = f'{self.base_file_path}/{file_path}'
    plt.savefig(file_saving_path,bbox_inches = 'tight')
    return file_path

  def create_mom_barplot(self,df,x_label,y_label,x_col,y_col):
    plt.figure(figsize=(12,6),dpi=100)
    sns.set_theme(style="whitegrid")
    ax = sns.barplot(x=df.loc[x_col],y=df.loc[y_col],palette="rocket")
    ax.set(xlabel=x_label, ylabel=y_label)
    ax.tick_params(axis='x', rotation=30)
    file_path = f'graph/bowlers/{uuid.uuid4()}.jpg'
    file_saving_path = f'{self.base_file_path}/{file_path}'
    plt.savefig(file_saving_path,bbox_inches = 'tight')
    return file_path
