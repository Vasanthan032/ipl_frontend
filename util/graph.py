import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

class Graph:
  def __init__(self):
    self.file_path = BASE_DIR.joinpath("users/static/graph/bowlers")

  def create_barplot(self,df,x_label,y_label,x_col,y_col):
    plt.figure(figsize=(12,6),dpi=100)
    sns.set_theme(style="whitegrid")
    ax = sns.barplot(x=x_col,y=y_col,data=df,palette="Set3")
    ax.set(xlabel=x_label, ylabel=y_label)
    ax.tick_params(axis='x', rotation=90)
    file_saving_path = f'{self.file_path}/top_10_bowlers.jpg' 
    plt.savefig(file_saving_path,bbox_inches = 'tight')
    return file_saving_path
