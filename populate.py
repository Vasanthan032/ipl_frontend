import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ipl.settings')

import django
django.setup()

from analysis.models import Batsman, Bowler, Stadium

def populate():

    top_batsman = [('DA Warner', 692),('KL Rahul', 593),('Q de Kock', 529),('S Dhawan', 521),('AD Russell', 510),('CH Gayle', 490),('RR Pant', 488),('V Kohli', 464),('SS Iyer', 463),('JM Bairstow', 445)]
    for i in range(len(top_batsman)):
        row = Batsman.objects.get_or_create(name = top_batsman[i][0], runs = int(top_batsman[i][1]))[0]

    top_bowler = [('Imran Tahir', 26),('K Rabada', 25),('DL Chahar', 22),('S Gopal', 20),('Mohammed Shami', 19),('KK Ahmed', 19),('JJ Bumrah', 19),('YS Chahal', 18),('Rashid Khan', 17),('SL Malinga', 16)]
    for i in range(len(top_bowler)):
        row = Bowler.objects.get_or_create(name = top_bowler[i][0], wickets = int(top_bowler[i][1]))[0]

    home_ground = [('Chennai Super Kings', 'MA Chidambaram Stadium, Chepauk'), ('Royal Challengers Bangalore','M Chinnaswamy Stadium'),('Kings XI Punjab','Punjab Cricket Association Stadium, Mohali'),('Kolkata Knight Riders','Eden Gardens'),('Mumbai Indians','Wankhede Stadium'),('Deccan Chargers','Rajiv Gandhi International Stadium, Uppal'),('Rajasthan Royals','Sardar Patel Stadium, Motera'),('Delhi Daredevils','Feroz Shah Kotla'),('Pune Warriors','Dr DY Patil Sports Academy'),('Kochi Tuskers Kerala','Nehru Stadium'),('Sunrisers Hyderabad','Rajiv Gandhi International Stadium, Uppal'),('Gujarat Lions','Saurashtra Cricket Association Stadium'),('Rising Pune Supergiant','Maharashtra Cricket Association Stadium')]
    for i in range(len(home_ground)):
        row = Stadium.objects.get_or_create(team = home_ground[i][0], ground = home_ground[i][1])[0]

if __name__ == '__main__':
    print("Populating datas")
    populate()
    print("Completed")
