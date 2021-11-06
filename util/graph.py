import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import uuid
BASE_DIR = Path(__file__).resolve().parent.parent

class Graph:
  def __init__(self):
    self.base_file_path = BASE_DIR.joinpath("users/static/")

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
    file_path = f'graph/bowlers/{uuid.uuid4()}.jpg'
    file_saving_path = f'{self.base_file_path}/{file_path}'
    plt.savefig(file_saving_path,bbox_inches = 'tight')
    return file_path


  def create_batsmen_barplot(self,df,year,category, x_label,y_label,x_col,y_col):
    plt.figure(figsize=(15,8),dpi=100)
    sns.set_theme(style="darkgrid")
    ax = sns.barplot(y=x_col,x=y_col,data=df,palette="Spectral")
    ax.set(xlabel=y_label, ylabel='')
    ax.set_title(f'{year.upper()} TOP10 {category.upper()}', size=15)

    for bar in ax.patches:
      ax.annotate('{:,.0f}'.format(bar.get_width()),
                   (bar.get_width(), bar.get_y() + bar.get_height() / 2),
                   size=12, xytext=(5, 0),
                   textcoords='offset points')

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
